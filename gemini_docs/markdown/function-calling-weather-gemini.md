**Note:** This version of the page covers the **Interactions API**. You can use the toggle on this page to switch to the [generateContent API version of this page](https://ai.google.dev/gemini-api/docs/generate-content/function-calling).

Function calling lets you connect models to external tools and APIs.
Instead of generating text responses, the model determines when to call specific
functions and provides the necessary parameters to execute real-world actions.
This allows the model to act as a bridge between natural language and real-world
actions and data. Function calling has 3 primary use cases:

- [**Take Actions:**](#meeting) Interact with external systems using APIs, such as scheduling appointments, creating invoices, sending emails, or controlling smart home devices.
- [**Augment Knowledge:**](#weather) Access information from external sources like databases, APIs, and knowledge bases.
- [**Extend Capabilities:**](#chart) Use external tools to perform computations and extend the limitations of the model, such as using a calculator or creating charts.

You can browse examples of these use cases below:

### Schedule Meeting

This example shows how to define a function that schedules a meeting with attendees at a specific time, allowing the model to parse user requests and return structured arguments to trigger actions in external systems.

### Get Weather

This example shows how to define a function that retrieves temperature data for a location, enabling the model to call external APIs to answer queries requiring real-time or external information.

### Create Chart

This example shows how to define a function that generates a bar chart from structured data, demonstrating how the model can use external tools to perform computations or create visual assets:

## How function calling works

Function calling involves a structured interaction between your application, the
model, and external functions:

This process can be repeated over multiple turns. The model supports calling
multiple functions in a single turn ([parallel function calling](https://ai.google.dev/gemini-api/docs/function-calling#parallel_function_calling)) and in
sequence ([compositional function calling](https://ai.google.dev/gemini-api/docs/function-calling#compositional_function_calling)).

### Step 1: Define a function declaration

### Step 2: Call the model with function declarations

The model returns a `function_call` step with `type`, `name`, and `arguments`:

### Step 3: Execute the function

### Step 4: Send result back to model

### Stateless function calling

You can also use function calling in stateless mode by managing the conversation history on the client side and setting `store=false`.

In stateless mode, you must pass the full history of the conversation in the `input` field of each subsequent request. This history must include:
1. The initial `user_input` step.
2. All model-generated steps returned in Turn 1 (including `thought` and `function_call` steps) exactly as received.
3. The `function_result` step containing the output of your executed function.

## Function declarations

A function declaration is passed as a tool and includes:

- `type` (string): Must be `"function"` for custom functions.
- `name` (string): Unique function name (use underscores or camelCase).
- `description` (string): Clear explanation of the function's purpose.
- `parameters` (object): Input parameters the function expects. `type` (string): Overall data type, such as `object`. `properties` (object): Individual parameters with type and description. `required` (array): Mandatory parameter names.

## Function calling with thinking models

Gemini 3 and 2.5 series models use an internal ["thinking"](https://ai.google.dev/gemini-api/docs/thinking) process that improves function calling.
The SDKs automatically handle [thought signatures](https://ai.google.dev/gemini-api/docs/thought-signatures) for you.

## Parallel function calling

Call multiple functions at once when they are independent:

## Compositional function calling

Chain multiple function calls together for complex requests (e.g., get location
first, then get weather for that location).

## Function calling modes

Control how the model uses tools using `tool_choice` in `generation_config`:

- `auto` (Default): Model decides whether to call a function or respond directly.
- `any`: Model is constrained to always predict a function call.
- `none`: Model is prohibited from making function calls.
- `validated` (Preview): Model ensures function schema adherence.

## Multi-tool use

You can enable multiple tools, combining built-in tools with function calling in
the same request. Gemini 3 models can combine built-in tools with function
calling out-of-the-box in Interactions. Passing `previous_interaction_id`
automatically circulates the built-in tool context.

## Multimodal function responses

For Gemini 3 series models, you can include multimodal content in
the function response parts that you send to the model. The model can process
this multimodal content in its next turn to produce a more informed response.

To include multimodal data in a function response, include it as one or more content blocks in the `result` field of the `function_result` step. Each content block must specify its `type` (e.g., `"text"`, `"image"`).

The following example shows how to send a function response containing image data back to the model in an interaction:

## Function calling with Structured output

For Gemini 3 series models, combine function calling with
[structured output](https://ai.google.dev/gemini-api/docs/structured-output) for
consistently formatted responses.

## Remote MCP (Model Context Protocol)

Interactions API supports connecting to remote MCP servers to give the model access to external tools and services. You provide the server `name` and `url` in the tools configuration.

When using Remote MCP, be aware of the following constraints:

- **Server types**: Remote MCP only works with Streamable HTTP servers. SSE (Server-Sent Events) servers are not supported.
- **Model support**: Remote MCP does not work with Gemini 3 models at this time. Support for Gemini 3 is coming soon.
- **Naming**: MCP server names should not include the `-` character. Use `snake_case` server names instead.

### Example

## Stream tool calls

When using tools with streaming, the model generates function calls as a
sequence of `step.delta` events on the stream. Tool arguments can be streamed
as partial arguments using `arguments`. You must aggregate these deltas to
reconstruct the complete tool calls before executing them.

## Best practices

- **Function and Parameter Descriptions:** Be clear and specific.
- **Naming:** Use descriptive names without spaces or special characters.
- **Strong Typing:** Use specific types (integer, string, enum).
- **Tool Selection:** Keep active set to 10-20 tools maximum.
- **Prompt Engineering:** Provide context and instructions.
- **Validation:** Validate function calls before executing.
- **Error Handling:** Implement robust error handling.
- **Security:** Use appropriate authentication for external APIs.

## Notes and limitations

- Only a [subset of the OpenAPI schema](https://ai.google.dev/api/rest/v1beta/cachedContents#FunctionDeclaration) is supported.
- For `any` mode, the API may reject very large or deeply nested schemas.
- Supported parameter types in Python are limited.
