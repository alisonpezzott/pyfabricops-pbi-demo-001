import sys
import os

# Add root directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts._pbi_cd_pipelines import pbi_enable_local_edit

pbi_enable_local_edit(
    project_path="src/PyFabricOps_Demo_001",
    workspace_alias="PyFabricOps_Demo_001",
)
