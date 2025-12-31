"""Agentic Context Engineering (ACE) reproduction framework."""

from typing import Optional

from .adaptation import (
    ACEBase,
    ACEStepResult,
    EnvironmentResult,
    OfflineACE,
    OnlineACE,
    Sample,
    SimpleEnvironment,
    TaskEnvironment,
)
from .async_learning import (
    AsyncLearningPipeline,
    LearningTask,
    ReflectionResult,
    ThreadSafeSkillbook,
)

# Import optional feature detection
from .features import has_litellm, has_opik
from .llm import DummyLLMClient, LLMClient, TransformersLLMClient
from .roles import (
    Agent,
    AgentOutput,
    Reflector,
    ReflectorOutput,
    ReplayAgent,
    SkillManager,
    SkillManagerOutput,
)
from .skillbook import Skill, Skillbook
from .updates import UpdateBatch, UpdateOperation

# Import observability components if available
if has_opik():
    try:
        from .observability import OpikIntegration as _OpikIntegration

        OpikIntegration: type | None = _OpikIntegration
        OBSERVABILITY_AVAILABLE = True
    except ImportError:
        OpikIntegration: type | None = None  # type: ignore
        OBSERVABILITY_AVAILABLE = False
else:
    OpikIntegration: type | None = None  # type: ignore
    OBSERVABILITY_AVAILABLE = False

# Import production LLM clients if available
if has_litellm():
    try:
        from .llm_providers import LiteLLMClient as _LiteLLMClient

        LiteLLMClient: type | None = _LiteLLMClient
        LITELLM_AVAILABLE = True
    except ImportError:
        LiteLLMClient: type | None = None  # type: ignore
        LITELLM_AVAILABLE = False
else:
    LiteLLMClient: type | None = None  # type: ignore
    LITELLM_AVAILABLE = False

# Import integrations (LiteLLM, browser-use, LangChain, Claude Code, etc.) if available
try:
    from .integrations import (
        BROWSER_USE_AVAILABLE as _BROWSER_USE_AVAILABLE,
    )
    from .integrations import (
        CLAUDE_CODE_AVAILABLE as _CLAUDE_CODE_AVAILABLE,
    )
    from .integrations import (
        LANGCHAIN_AVAILABLE as _LANGCHAIN_AVAILABLE,
    )
    from .integrations import (
        ACEAgent as _ACEAgent,
    )
    from .integrations import (
        ACEClaudeCode as _ACEClaudeCode,
    )
    from .integrations import (
        ACELangChain as _ACELangChain,
    )
    from .integrations import (
        ACELiteLLM as _ACELiteLLM,
    )
    from .integrations import (
        wrap_skillbook_context as _wrap_skillbook_context,
    )

    ACELiteLLM: type | None = _ACELiteLLM
    ACEAgent: type | None = _ACEAgent
    ACELangChain: type | None = _ACELangChain
    ACEClaudeCode: type | None = _ACEClaudeCode
    wrap_skillbook_context: type | None = _wrap_skillbook_context  # type: ignore
    BROWSER_USE_AVAILABLE = _BROWSER_USE_AVAILABLE
    LANGCHAIN_AVAILABLE = _LANGCHAIN_AVAILABLE
    CLAUDE_CODE_AVAILABLE = _CLAUDE_CODE_AVAILABLE
except ImportError:
    ACELiteLLM: type | None = None  # type: ignore
    ACEAgent: type | None = None  # type: ignore
    ACELangChain: type | None = None  # type: ignore
    ACEClaudeCode: type | None = None  # type: ignore
    wrap_skillbook_context: type | None = None  # type: ignore
    BROWSER_USE_AVAILABLE = False
    LANGCHAIN_AVAILABLE = False
    CLAUDE_CODE_AVAILABLE = False

# Import deduplication module
from .deduplication import (
    DeduplicationConfig,
    DeduplicationManager,
)

__all__ = [
    # Core components
    "Skill",
    "Skillbook",
    "UpdateOperation",
    "UpdateBatch",
    "LLMClient",
    "DummyLLMClient",
    "TransformersLLMClient",
    "LiteLLMClient",
    "Agent",
    "ReplayAgent",
    "Reflector",
    "SkillManager",
    "AgentOutput",
    "ReflectorOutput",
    "SkillManagerOutput",
    "OfflineACE",
    "OnlineACE",
    "ACEBase",
    "Sample",
    "TaskEnvironment",
    "SimpleEnvironment",
    "EnvironmentResult",
    "ACEStepResult",
    # Deduplication
    "DeduplicationConfig",
    "DeduplicationManager",
    # Out-of-box integrations
    "ACELiteLLM",  # LiteLLM integration (quick start)
    "ACEAgent",  # Browser-use integration
    "ACELangChain",  # LangChain integration (complex workflows)
    "ACEClaudeCode",  # Claude Code CLI integration
    # Utilities
    "wrap_skillbook_context",
    # Async learning
    "LearningTask",
    "ReflectionResult",
    "ThreadSafeSkillbook",
    "AsyncLearningPipeline",
    # Feature flags
    "OpikIntegration",
    "LITELLM_AVAILABLE",
    "OBSERVABILITY_AVAILABLE",
    "BROWSER_USE_AVAILABLE",
    "LANGCHAIN_AVAILABLE",
    "CLAUDE_CODE_AVAILABLE",
]
