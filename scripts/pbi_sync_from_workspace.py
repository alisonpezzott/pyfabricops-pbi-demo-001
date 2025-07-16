import sys
import os

# Add root directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts._pbi_cd_pipelines import pbi_sync_from_workspace

pbi_sync_from_workspace(
    project="PyFabricOps_Demo_001",
    workspace_alias="PyFabricOps_Demo_001",
    project_path="src/PyFabricOps_Demo_001",
)