from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field

from letta.schemas.embedding_config import EmbeddingConfig
from letta.schemas.llm_config import LLMConfig


class CoreMemoryBlockSchema(BaseModel):
    created_at: str
    description: Optional[str]
    identities: List[Any]
    is_deleted: bool
    is_template: bool
    label: str
    limit: int
    metadata_: Dict[str, Any] = Field(default_factory=dict)
    template_name: Optional[str]
    updated_at: str
    value: str


class MessageSchema(BaseModel):
    created_at: str
    group_id: Optional[str]
    in_context: bool
    model: Optional[str]
    name: Optional[str]
    role: str
    text: str
    tool_call_id: Optional[str]
    tool_calls: List[Any]
    tool_returns: List[Any]
    updated_at: str


class TagSchema(BaseModel):
    tag: str


class ToolEnvVarSchema(BaseModel):
    created_at: str
    description: Optional[str]
    is_deleted: bool
    key: str
    updated_at: str
    value: str


class ToolRuleSchema(BaseModel):
    tool_name: str
    type: str


class ParameterProperties(BaseModel):
    type: str
    description: Optional[str] = None


class ParametersSchema(BaseModel):
    type: Optional[str] = "object"
    properties: Dict[str, ParameterProperties]
    required: List[str] = Field(default_factory=list)


class ToolJSONSchema(BaseModel):
    name: str
    description: str
    parameters: ParametersSchema  # <— nested strong typing
    type: Optional[str] = None  # top-level 'type' if it exists
    required: Optional[List[str]] = Field(default_factory=list)


class ToolSchema(BaseModel):
    args_json_schema: Optional[Any]
    created_at: str
    description: str
    is_deleted: bool
    json_schema: ToolJSONSchema
    name: str
    return_char_limit: int
    source_code: Optional[str]
    source_type: str
    tags: List[str]
    tool_type: str
    updated_at: str


class AgentSchema(BaseModel):
    agent_type: str
    core_memory: List[CoreMemoryBlockSchema]
    created_at: str
    description: str
    embedding_config: EmbeddingConfig
    groups: List[Any]
    identities: List[Any]
    is_deleted: bool
    llm_config: LLMConfig
    message_buffer_autoclear: bool
    messages: List[MessageSchema]
    metadata_: Dict
    multi_agent_group: Optional[Any]
    name: str
    system: str
    tags: List[TagSchema]
    tool_exec_environment_variables: List[ToolEnvVarSchema]
    tool_rules: List[ToolRuleSchema]
    tools: List[ToolSchema]
    updated_at: str
    version: str
