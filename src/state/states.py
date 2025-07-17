from typing_extensions import TypedDict
from typing import Union, Optional, Dict

class state(TypedDict):
    """
    Shared state structure passed between LangGraph nodes.

    Attributes:
        input (str): The user’s query.
        format (str): Either "text" or "json", controlling response format.
        fields (dict): Expected JSON schema when format is "json".
        tool_response (Optional[str]): Raw tool output (if any).
        output (Optional[Union[str, dict]]): Final LLM or tool answer.
    """
    input: str
    format: str  # "json" or "text"
    fields: Dict[str, str]
    tool_response: Optional[str]
    output: Optional[Union[str, dict]]
