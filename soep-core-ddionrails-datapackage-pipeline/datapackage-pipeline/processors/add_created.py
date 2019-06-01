# Add created timestamp
from datetime import datetime, timezone
from datapackage_pipelines.wrapper import process

def modify_datapackage(datapackage, parameters, stats):
    local_time = datetime.now(timezone.utc).astimezone()
    timestamp = local_time.isoformat()
    datapackage['created'] = timestamp
    return datapackage

process(modify_datapackage=modify_datapackage)