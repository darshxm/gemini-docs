from gemini_docs.models import DocumentSpec

DOCUMENT_SPECS = [
    DocumentSpec(
        slug="text-generation",
        title="Text Generation",
        url="https://ai.google.dev/gemini-api/docs/text-generation",
        module_name="text_generation",
        markdown_filename="text-generation-gemini.md",
    ),
    DocumentSpec(
        slug="document-processing",
        title="Document Processing",
        url="https://ai.google.dev/gemini-api/docs/document-processing",
        module_name="document_processing",
        markdown_filename="document-processing-gemini.md",
    ),
    DocumentSpec(
        slug="structured-output-recipe",
        title="Structured Output Recipe",
        url="https://ai.google.dev/gemini-api/docs/structured-output?example=recipe",
        module_name="structured_output_recipe",
        markdown_filename="structured-output-recipe-gemini.md",
    ),
    DocumentSpec(
        slug="structured-output-feedback",
        title="Structured Output Feedback",
        url="https://ai.google.dev/gemini-api/docs/structured-output?example=feedback",
        module_name="structured_output_feedback",
        markdown_filename="structured-output-feedback-gemini.md",
    ),
    DocumentSpec(
        slug="structured-output-recursive",
        title="Structured Output Recursive",
        url="https://ai.google.dev/gemini-api/docs/structured-output?example=recursive",
        module_name="structured_output_recursive",
        markdown_filename="structured-output-recursive-gemini.md",
    ),
    DocumentSpec(
        slug="function-calling-meeting",
        title="Function Calling Meeting",
        url="https://ai.google.dev/gemini-api/docs/function-calling?example=meeting",
        module_name="function_calling_meeting",
        markdown_filename="function-calling-meeting-gemini.md",
    ),
    DocumentSpec(
        slug="function-calling-weather",
        title="Function Calling Weather",
        url="https://ai.google.dev/gemini-api/docs/function-calling?example=weather",
        module_name="function_calling_weather",
        markdown_filename="function-calling-weather-gemini.md",
    ),
    DocumentSpec(
        slug="function-calling-chart",
        title="Function Calling Chart",
        url="https://ai.google.dev/gemini-api/docs/function-calling?example=chart",
        module_name="function_calling_chart",
        markdown_filename="function-calling-chart-gemini.md",
    ),
]

DOCUMENT_SPECS_BY_SLUG = {spec.slug: spec for spec in DOCUMENT_SPECS}
