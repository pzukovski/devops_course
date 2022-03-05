dict ={'changed': False, 'datastores': [{'accessible': True, 'capacity': 3298266447872, 'name': 'CISVM_RM_Templates_N10_vmfs5_249', 'freeSpace': 1196335038464, 'maintenanceMode': 'normal', 'multipleHostAccess': True, 'type': 'VMFS', 'uncommitted': 12935843097157, 'url': 'ds:///vmfs/volumes/57308adc-49a8c2ed-2a7b-80c16eaaee18/', 'provisioned': 15037774506565, 'datastore_cluster': 'N/A'}, {'accessible': True, 'capacity': 1099780063232, 'name': 'CIHCI-SSD-RP-HCI-Backend-1', 'freeSpace': 765716332544, 'maintenanceMode': 'normal', 'multipleHostAccess': True, 'type': 'VMFS', 'uncommitted': 1045828573920, 'url': 'ds:///vmfs/volumes/619e17cb-701d2604-00eb-ac1f6bca77e2/', 'provisioned': 1379892304608, 'datastore_cluster': 'CI-HCI_Backend1'}], 'failed': False}



for key,values in dict.items():
     for v in values:
          print(int(key," : ",v))
