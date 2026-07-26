def validate_llm_response(response) -> str:
    """
    Validate the response returned by an LLM and return its text content.

    Raises:
        TypeError: If response.content is not a string.
        ValueError: If the response content is empty.
    """
    content = response.content

    if not isinstance(content, str):
        raise TypeError(
            f"Expected response.content to be a string, got {type(content).__name__}.")

    content = content.strip()

    if not content:
        raise ValueError("LLM returned an empty response.")

    return content