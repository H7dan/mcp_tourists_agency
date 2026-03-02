## Orchestrator ↔ LLM interaction

This document describes only the internal interaction between the **orchestrator** and the **LLM with MCP tools**. The Telegram bot and other clients are out of scope here.

### Role of `llm_chat.py`

- Module `services/orchestrator/api/llm_chat.py`:
  - receives a ready `OrchestratorRequest` from the HTTP layer;
  - builds a request to the LLM (dialog context, system instructions, list of tools);
  - runs the LLM ↔ tools loop until a final answer is produced;
  - returns an `OrchestratorResponse` with user-facing text or an error code.

### LLM + tools loop

1. Build an LLM request: current conversation history + latest user message + descriptions of available MCP tools.  
2. Send the request to the LLM and inspect the response:
   - if it is a **final answer**, return it as `OrchestratorResponse.success(text)`;
   - if it is a **tool call**, extract the tool name and arguments.
3. Call the requested MCP tool, get the result, and append it to the conversation history as a `tool` message.  
4. Call the LLM again with the updated history.  
5. Repeat steps 2–4 until the LLM returns a final human-readable answer without a tool call.

### Data sent from orchestrator to LLM

Minimum data included in an LLM request:

- **system and developer instructions** — who the assistant is, how it should respond, and what constraints apply;
- **conversation history** — previous `user` / `assistant` / `tool` messages for the last several turns;
- **current user message** — text from `OrchestratorRequest.text`;
- **user metadata** — for example `user_id`, language, and optional preferences;
- **MCP tool descriptions** — names, parameters, and short purpose of each available tool;
- **LLM generation parameters** — temperature, maximum response length, and other model settings.

