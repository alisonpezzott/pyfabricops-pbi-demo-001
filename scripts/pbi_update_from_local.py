import sys
import os

# Add root directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts._pbi_cd_pipelines import pbi_update_from_local

pbi_update_from_local(
    project="PyFabricOps_Demo_001",
    workspace_alias="PyFabricOps_Demo_001",
    project_path="src/PyFabricOps_Demo_001",
    dataflows_gen1=['Date.Dataflow'],
)
    