from enum import Enum


class SwarmSpecSwarmTypeType0(str, Enum):
    AGENTREARRANGE = "AgentRearrange"
    AUTO = "auto"
    AUTOSWARMBUILDER = "AutoSwarmBuilder"
    CONCURRENTWORKFLOW = "ConcurrentWorkflow"
    COUNCILASAJUDGE = "CouncilAsAJudge"
    DEEPRESEARCHSWARM = "DeepResearchSwarm"
    GROUPCHAT = "GroupChat"
    HIEARCHICALSWARM = "HiearchicalSwarm"
    INTERACTIVEGROUPCHAT = "InteractiveGroupChat"
    MAJORITYVOTING = "MajorityVoting"
    MALT = "MALT"
    MIXTUREOFAGENTS = "MixtureOfAgents"
    MULTIAGENTROUTER = "MultiAgentRouter"
    SEQUENTIALWORKFLOW = "SequentialWorkflow"
    SPREADSHEETSWARM = "SpreadSheetSwarm"

    def __str__(self) -> str:
        return str(self.value)
