# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_mock_integration"""

from __future__ import print_function
from resilient_circuits.util import *

def codegen_reload_data():
    """Parameters to codegen used to generate the fn_mock_integration package"""
    reload_params = {"package": u"fn_mock_integration",
                    "incident_fields": [u"mock_incident_field"], 
                    "action_fields": [u"mock_activity_field_one"], 
                    "function_params": [u"mock_field_one", u"mock_field_two"], 
                    "datatables": [u"mock_data_table"], 
                    "message_destinations": [u"fn_mock_integration"], 
                    "functions": [u"mock_function_one", u"mock_function_two"], 
                    "phases": [], 
                    "automatic_tasks": [], 
                    "scripts": [], 
                    "workflows": [u"example_mock_workflow_one"], 
                    "actions": [u"Mock Auto Rule", u"Mock Manual Rule"], 
                    "incident_artifact_types": [] 
                    }
    return reload_params


def customization_data(client=None):
    """Produce any customization definitions (types, fields, message destinations, etc)
       that should be installed by `resilient-circuits customize`
    """

    # This import data contains:
    #   Incident fields:
    #     mock_incident_field
    #   Action fields:
    #     mock_activity_field_one
    #   Function inputs:
    #     mock_field_one
    #     mock_field_two
    #   DataTables:
    #     mock_data_table
    #   Message Destinations:
    #     fn_mock_integration
    #   Functions:
    #     mock_function_one
    #     mock_function_two
    #   Workflows:
    #     example_mock_workflow_one
    #   Rules:
    #     Mock Auto Rule
    #     Mock Manual Rule


    yield ImportDefinition(u"""
eyJsb2NhbGUiOiBudWxsLCAid29ya2Zsb3dzIjogW3siZGVzY3JpcHRpb24iOiAiQW4gZXhhbXBs
ZSB3b3JrZmxvdyBmb3IgbW9jayB1bml0IHRlc3RzIiwgIndvcmtmbG93X2lkIjogNywgInRhZ3Mi
OiBbXSwgIm9iamVjdF90eXBlIjogImluY2lkZW50IiwgImV4cG9ydF9rZXkiOiAiZXhhbXBsZV9t
b2NrX3dvcmtmbG93X29uZSIsICJ1dWlkIjogImZhZDMxNzM5LTA2MzQtNDJjOS1hMDBhLTcwZTY2
MTA3NDA4YiIsICJhY3Rpb25zIjogW10sICJjb250ZW50IjogeyJ4bWwiOiAiPD94bWwgdmVyc2lv
bj1cIjEuMFwiIGVuY29kaW5nPVwiVVRGLThcIj8+PGRlZmluaXRpb25zIHhtbG5zPVwiaHR0cDov
L3d3dy5vbWcub3JnL3NwZWMvQlBNTi8yMDEwMDUyNC9NT0RFTFwiIHhtbG5zOmJwbW5kaT1cImh0
dHA6Ly93d3cub21nLm9yZy9zcGVjL0JQTU4vMjAxMDA1MjQvRElcIiB4bWxuczpvbWdkYz1cImh0
dHA6Ly93d3cub21nLm9yZy9zcGVjL0RELzIwMTAwNTI0L0RDXCIgeG1sbnM6b21nZGk9XCJodHRw
Oi8vd3d3Lm9tZy5vcmcvc3BlYy9ERC8yMDEwMDUyNC9ESVwiIHhtbG5zOnJlc2lsaWVudD1cImh0
dHA6Ly9yZXNpbGllbnQuaWJtLmNvbS9icG1uXCIgeG1sbnM6eHNkPVwiaHR0cDovL3d3dy53My5v
cmcvMjAwMS9YTUxTY2hlbWFcIiB4bWxuczp4c2k9XCJodHRwOi8vd3d3LnczLm9yZy8yMDAxL1hN
TFNjaGVtYS1pbnN0YW5jZVwiIHRhcmdldE5hbWVzcGFjZT1cImh0dHA6Ly93d3cuY2FtdW5kYS5v
cmcvdGVzdFwiPjxwcm9jZXNzIGlkPVwiZXhhbXBsZV9tb2NrX3dvcmtmbG93X29uZVwiIGlzRXhl
Y3V0YWJsZT1cInRydWVcIiBuYW1lPVwiRXhhbXBsZTogTW9jayBXb3JrZmxvdyBPbmVcIj48ZG9j
dW1lbnRhdGlvbj5BbiBleGFtcGxlIHdvcmtmbG93IGZvciBtb2NrIHVuaXQgdGVzdHM8L2RvY3Vt
ZW50YXRpb24+PHN0YXJ0RXZlbnQgaWQ9XCJTdGFydEV2ZW50XzE1NWFzeG1cIj48b3V0Z29pbmc+
U2VxdWVuY2VGbG93XzAxMmxjazA8L291dGdvaW5nPjwvc3RhcnRFdmVudD48c2VydmljZVRhc2sg
aWQ9XCJTZXJ2aWNlVGFza18xOGE5M3hlXCIgbmFtZT1cIm1vY2tfZnVuY3Rpb25fb25lXCIgcmVz
aWxpZW50OnR5cGU9XCJmdW5jdGlvblwiPjxleHRlbnNpb25FbGVtZW50cz48cmVzaWxpZW50OmZ1
bmN0aW9uIHV1aWQ9XCI5NmNjNjQ1YS1iOTc3LTRkYzktOWQxZC1jYWRiNDA4MGJiN2FcIj57XCJp
bnB1dHNcIjp7XCIxNjkzMzg1Mi03MTJjLTRlM2ItYjc4NS03Yzk5NTE0ZTk1NTFcIjp7XCJpbnB1
dF90eXBlXCI6XCJzdGF0aWNcIixcInN0YXRpY19pbnB1dFwiOntcIm11bHRpc2VsZWN0X3ZhbHVl
XCI6W10sXCJ0ZXh0X3ZhbHVlXCI6XCJtb2NrIGlucHV0IHZhbHVlIG9uZVwifX0sXCJhMTYxMjIz
Yy05YzYwLTQ4MGYtOGIyMC01OTc0M2U2NGRkNTNcIjp7XCJpbnB1dF90eXBlXCI6XCJzdGF0aWNc
IixcInN0YXRpY19pbnB1dFwiOntcIm11bHRpc2VsZWN0X3ZhbHVlXCI6W10sXCJudW1iZXJfdmFs
dWVcIjoxMjM0NX19fX08L3Jlc2lsaWVudDpmdW5jdGlvbj48L2V4dGVuc2lvbkVsZW1lbnRzPjxp
bmNvbWluZz5TZXF1ZW5jZUZsb3dfMDEybGNrMDwvaW5jb21pbmc+PG91dGdvaW5nPlNlcXVlbmNl
Rmxvd18wNWw2MzZpPC9vdXRnb2luZz48L3NlcnZpY2VUYXNrPjxlbmRFdmVudCBpZD1cIkVuZEV2
ZW50XzByZmhtZXNcIj48aW5jb21pbmc+U2VxdWVuY2VGbG93XzF0ZWo0bm08L2luY29taW5nPjwv
ZW5kRXZlbnQ+PHNlcXVlbmNlRmxvdyBpZD1cIlNlcXVlbmNlRmxvd18wMTJsY2swXCIgc291cmNl
UmVmPVwiU3RhcnRFdmVudF8xNTVhc3htXCIgdGFyZ2V0UmVmPVwiU2VydmljZVRhc2tfMThhOTN4
ZVwiLz48c2VxdWVuY2VGbG93IGlkPVwiU2VxdWVuY2VGbG93XzA1bDYzNmlcIiBzb3VyY2VSZWY9
XCJTZXJ2aWNlVGFza18xOGE5M3hlXCIgdGFyZ2V0UmVmPVwiU2VydmljZVRhc2tfMWVhdHdtcVwi
Lz48c2VydmljZVRhc2sgaWQ9XCJTZXJ2aWNlVGFza18xZWF0d21xXCIgbmFtZT1cIm1vY2tfZnVu
Y3Rpb25fdHdvXCIgcmVzaWxpZW50OnR5cGU9XCJmdW5jdGlvblwiPjxleHRlbnNpb25FbGVtZW50
cz48cmVzaWxpZW50OmZ1bmN0aW9uIHV1aWQ9XCJkODRhMzliOS00NzI2LTQzOTAtOTI5NC0xNTI1
MTc0ZDQxY2NcIj57XCJpbnB1dHNcIjp7fSxcInBvc3RfcHJvY2Vzc2luZ19zY3JpcHRcIjpcImlu
Y2lkZW50LmFkZE5vdGUoXFxcImEgbW9jayBub3RlIGFkZGVkIGluIHRoZSBwb3N0IHByb2Nlc3Mg
c2NyaXB0XFxcIilcIixcInByZV9wcm9jZXNzaW5nX3NjcmlwdFwiOlwiXFxuaW5wdXRzLm1vY2tf
ZmllbGRfb25lID0gXFxcIm1vY2sgdmFsdWUgZm9yIGZpZWxkIG9uZVxcXCJcXG5cXG5pbnB1dHMu
bW9ja19maWVsZF90d28gPSAxMjM0NVwifTwvcmVzaWxpZW50OmZ1bmN0aW9uPjwvZXh0ZW5zaW9u
RWxlbWVudHM+PGluY29taW5nPlNlcXVlbmNlRmxvd18wNWw2MzZpPC9pbmNvbWluZz48b3V0Z29p
bmc+U2VxdWVuY2VGbG93XzF0ZWo0bm08L291dGdvaW5nPjwvc2VydmljZVRhc2s+PHNlcXVlbmNl
RmxvdyBpZD1cIlNlcXVlbmNlRmxvd18xdGVqNG5tXCIgc291cmNlUmVmPVwiU2VydmljZVRhc2tf
MWVhdHdtcVwiIHRhcmdldFJlZj1cIkVuZEV2ZW50XzByZmhtZXNcIi8+PC9wcm9jZXNzPjxicG1u
ZGk6QlBNTkRpYWdyYW0gaWQ9XCJCUE1ORGlhZ3JhbV8xXCI+PGJwbW5kaTpCUE1OUGxhbmUgYnBt
bkVsZW1lbnQ9XCJ1bmRlZmluZWRcIiBpZD1cIkJQTU5QbGFuZV8xXCI+PGJwbW5kaTpCUE1OU2hh
cGUgYnBtbkVsZW1lbnQ9XCJTdGFydEV2ZW50XzE1NWFzeG1cIiBpZD1cIlN0YXJ0RXZlbnRfMTU1
YXN4bV9kaVwiPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMzZcIiB3aWR0aD1cIjM2XCIgeD1cIjM5
NlwiIHk9XCI2OVwiLz48YnBtbmRpOkJQTU5MYWJlbD48b21nZGM6Qm91bmRzIGhlaWdodD1cIjBc
IiB3aWR0aD1cIjkwXCIgeD1cIjM5MVwiIHk9XCIxMDRcIi8+PC9icG1uZGk6QlBNTkxhYmVsPjwv
YnBtbmRpOkJQTU5TaGFwZT48YnBtbmRpOkJQTU5TaGFwZSBicG1uRWxlbWVudD1cIlNlcnZpY2VU
YXNrXzE4YTkzeGVcIiBpZD1cIlNlcnZpY2VUYXNrXzE4YTkzeGVfZGlcIj48b21nZGM6Qm91bmRz
IGhlaWdodD1cIjgwXCIgd2lkdGg9XCIxMDBcIiB4PVwiNTUzXCIgeT1cIjQ3XCIvPjwvYnBtbmRp
OkJQTU5TaGFwZT48YnBtbmRpOkJQTU5TaGFwZSBicG1uRWxlbWVudD1cIkVuZEV2ZW50XzByZmht
ZXNcIiBpZD1cIkVuZEV2ZW50XzByZmhtZXNfZGlcIj48b21nZGM6Qm91bmRzIGhlaWdodD1cIjM2
XCIgd2lkdGg9XCIzNlwiIHg9XCIxMDMwXCIgeT1cIjY5XCIvPjxicG1uZGk6QlBNTkxhYmVsPjxv
bWdkYzpCb3VuZHMgaGVpZ2h0PVwiMTNcIiB3aWR0aD1cIjBcIiB4PVwiMTA0OFwiIHk9XCIxMDhc
Ii8+PC9icG1uZGk6QlBNTkxhYmVsPjwvYnBtbmRpOkJQTU5TaGFwZT48YnBtbmRpOkJQTU5FZGdl
IGJwbW5FbGVtZW50PVwiU2VxdWVuY2VGbG93XzAxMmxjazBcIiBpZD1cIlNlcXVlbmNlRmxvd18w
MTJsY2swX2RpXCI+PG9tZ2RpOndheXBvaW50IHg9XCI0MzJcIiB4c2k6dHlwZT1cIm9tZ2RjOlBv
aW50XCIgeT1cIjg3XCIvPjxvbWdkaTp3YXlwb2ludCB4PVwiNTUzXCIgeHNpOnR5cGU9XCJvbWdk
YzpQb2ludFwiIHk9XCI4N1wiLz48YnBtbmRpOkJQTU5MYWJlbD48b21nZGM6Qm91bmRzIGhlaWdo
dD1cIjEzXCIgd2lkdGg9XCIwXCIgeD1cIjQ5Mi41XCIgeT1cIjY1XCIvPjwvYnBtbmRpOkJQTU5M
YWJlbD48L2JwbW5kaTpCUE1ORWRnZT48YnBtbmRpOkJQTU5FZGdlIGJwbW5FbGVtZW50PVwiU2Vx
dWVuY2VGbG93XzA1bDYzNmlcIiBpZD1cIlNlcXVlbmNlRmxvd18wNWw2MzZpX2RpXCI+PG9tZ2Rp
OndheXBvaW50IHg9XCI2NTNcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjg3XCIvPjxv
bWdkaTp3YXlwb2ludCB4PVwiNzgxXCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCI4N1wi
Lz48YnBtbmRpOkJQTU5MYWJlbD48b21nZGM6Qm91bmRzIGhlaWdodD1cIjEzXCIgd2lkdGg9XCIw
XCIgeD1cIjcxN1wiIHk9XCI2NS41XCIvPjwvYnBtbmRpOkJQTU5MYWJlbD48L2JwbW5kaTpCUE1O
RWRnZT48YnBtbmRpOkJQTU5TaGFwZSBicG1uRWxlbWVudD1cIlNlcnZpY2VUYXNrXzFlYXR3bXFc
IiBpZD1cIlNlcnZpY2VUYXNrXzFlYXR3bXFfZGlcIj48b21nZGM6Qm91bmRzIGhlaWdodD1cIjgw
XCIgd2lkdGg9XCIxMDBcIiB4PVwiNzgxXCIgeT1cIjQ3XCIvPjwvYnBtbmRpOkJQTU5TaGFwZT48
YnBtbmRpOkJQTU5FZGdlIGJwbW5FbGVtZW50PVwiU2VxdWVuY2VGbG93XzF0ZWo0bm1cIiBpZD1c
IlNlcXVlbmNlRmxvd18xdGVqNG5tX2RpXCI+PG9tZ2RpOndheXBvaW50IHg9XCI4ODFcIiB4c2k6
dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjg3XCIvPjxvbWdkaTp3YXlwb2ludCB4PVwiMTAzMFwi
IHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiODdcIi8+PGJwbW5kaTpCUE1OTGFiZWw+PG9t
Z2RjOkJvdW5kcyBoZWlnaHQ9XCIxM1wiIHdpZHRoPVwiMFwiIHg9XCI5NTUuNVwiIHk9XCI2NVwi
Lz48L2JwbW5kaTpCUE1OTGFiZWw+PC9icG1uZGk6QlBNTkVkZ2U+PC9icG1uZGk6QlBNTlBsYW5l
PjwvYnBtbmRpOkJQTU5EaWFncmFtPjwvZGVmaW5pdGlvbnM+IiwgIndvcmtmbG93X2lkIjogImV4
YW1wbGVfbW9ja193b3JrZmxvd19vbmUiLCAidmVyc2lvbiI6IDN9LCAiY3JlYXRvcl9pZCI6ICJh
ZG1pbkBleGFtcGxlLmNvbSIsICJsYXN0X21vZGlmaWVkX2J5IjogImFkbWluQGV4YW1wbGUuY29t
IiwgImxhc3RfbW9kaWZpZWRfdGltZSI6IDE1NTgwODMzNjcwNzEsICJjb250ZW50X3ZlcnNpb24i
OiAzLCAicHJvZ3JhbW1hdGljX25hbWUiOiAiZXhhbXBsZV9tb2NrX3dvcmtmbG93X29uZSIsICJu
YW1lIjogIkV4YW1wbGU6IE1vY2sgV29ya2Zsb3cgT25lIn1dLCAiYWN0aW9ucyI6IFt7InRpbWVv
dXRfc2Vjb25kcyI6IDg2NDAwLCAib2JqZWN0X3R5cGUiOiAiaW5jaWRlbnQiLCAidHlwZSI6IDAs
ICJuYW1lIjogIk1vY2sgQXV0byBSdWxlIiwgInRhZ3MiOiBbXSwgInZpZXdfaXRlbXMiOiBbXSwg
ImVuYWJsZWQiOiB0cnVlLCAid29ya2Zsb3dzIjogWyJleGFtcGxlX21vY2tfd29ya2Zsb3dfb25l
Il0sICJsb2dpY190eXBlIjogImFsbCIsICJleHBvcnRfa2V5IjogIk1vY2sgQXV0byBSdWxlIiwg
InV1aWQiOiAiNWI2MGE5ODMtOWM1YS00MWY0LWI2OGItYWU2NGYwMzhiNzEyIiwgImF1dG9tYXRp
b25zIjogW10sICJjb25kaXRpb25zIjogW3sidHlwZSI6IG51bGwsICJldmFsdWF0aW9uX2lkIjog
bnVsbCwgImZpZWxkX25hbWUiOiBudWxsLCAibWV0aG9kIjogIm9iamVjdF9hZGRlZCIsICJ2YWx1
ZSI6IG51bGx9XSwgImlkIjogMjEsICJtZXNzYWdlX2Rlc3RpbmF0aW9ucyI6IFtdfSwgeyJ0aW1l
b3V0X3NlY29uZHMiOiA4NjQwMCwgIm9iamVjdF90eXBlIjogImluY2lkZW50IiwgInR5cGUiOiAx
LCAibmFtZSI6ICJNb2NrIE1hbnVhbCBSdWxlIiwgInRhZ3MiOiBbXSwgInZpZXdfaXRlbXMiOiBb
eyJzaG93X2lmIjogbnVsbCwgImZpZWxkX3R5cGUiOiAiYWN0aW9uaW52b2NhdGlvbiIsICJzaG93
X2xpbmtfaGVhZGVyIjogZmFsc2UsICJlbGVtZW50IjogImZpZWxkX3V1aWQiLCAiY29udGVudCI6
ICJmMWQ1NDE5Zi1kYjg5LTRiNmMtYTdmMC0xMDU1OWE2ZTM2YzIiLCAic3RlcF9sYWJlbCI6IG51
bGx9XSwgImVuYWJsZWQiOiB0cnVlLCAid29ya2Zsb3dzIjogWyJleGFtcGxlX21vY2tfd29ya2Zs
b3dfb25lIl0sICJsb2dpY190eXBlIjogImFsbCIsICJleHBvcnRfa2V5IjogIk1vY2sgTWFudWFs
IFJ1bGUiLCAidXVpZCI6ICI2NGFhMzhjMS02ZmNlLTQzYjktYjc4Zi0zMjNhMTU2OGYyNDQiLCAi
YXV0b21hdGlvbnMiOiBbXSwgImNvbmRpdGlvbnMiOiBbXSwgImlkIjogMjAsICJtZXNzYWdlX2Rl
c3RpbmF0aW9ucyI6IFtdfV0sICJsYXlvdXRzIjogW10sICJleHBvcnRfZm9ybWF0X3ZlcnNpb24i
OiAyLCAiaWQiOiAxLCAiaW5kdXN0cmllcyI6IG51bGwsICJmdW5jdGlvbnMiOiBbeyJkaXNwbGF5
X25hbWUiOiAibW9ja19mdW5jdGlvbl9vbmUiLCAiZGVzY3JpcHRpb24iOiB7ImNvbnRlbnQiOiAi
bW9ja19kZXNjcmlwdGlvbiIsICJmb3JtYXQiOiAidGV4dCJ9LCAiY3JlYXRvciI6IHsidHlwZSI6
ICJ1c2VyIiwgImRpc3BsYXlfbmFtZSI6ICJBZG1pbiBVc2VyIiwgImlkIjogNzEsICJuYW1lIjog
ImFkbWluQGV4YW1wbGUuY29tIn0sICJ2aWV3X2l0ZW1zIjogW3sic2hvd19pZiI6IG51bGwsICJm
aWVsZF90eXBlIjogIl9fZnVuY3Rpb24iLCAic2hvd19saW5rX2hlYWRlciI6IGZhbHNlLCAiZWxl
bWVudCI6ICJmaWVsZF91dWlkIiwgImNvbnRlbnQiOiAiMTY5MzM4NTItNzEyYy00ZTNiLWI3ODUt
N2M5OTUxNGU5NTUxIiwgInN0ZXBfbGFiZWwiOiBudWxsfSwgeyJzaG93X2lmIjogbnVsbCwgImZp
ZWxkX3R5cGUiOiAiX19mdW5jdGlvbiIsICJzaG93X2xpbmtfaGVhZGVyIjogZmFsc2UsICJlbGVt
ZW50IjogImZpZWxkX3V1aWQiLCAiY29udGVudCI6ICJhMTYxMjIzYy05YzYwLTQ4MGYtOGIyMC01
OTc0M2U2NGRkNTMiLCAic3RlcF9sYWJlbCI6IG51bGx9XSwgInRhZ3MiOiBbXSwgImV4cG9ydF9r
ZXkiOiAibW9ja19mdW5jdGlvbl9vbmUiLCAidXVpZCI6ICI5NmNjNjQ1YS1iOTc3LTRkYzktOWQx
ZC1jYWRiNDA4MGJiN2EiLCAibGFzdF9tb2RpZmllZF9ieSI6IHsidHlwZSI6ICJ1c2VyIiwgImRp
c3BsYXlfbmFtZSI6ICJBZG1pbiBVc2VyIiwgImlkIjogNzEsICJuYW1lIjogImFkbWluQGV4YW1w
bGUuY29tIn0sICJ2ZXJzaW9uIjogMSwgIndvcmtmbG93cyI6IFt7InByb2dyYW1tYXRpY19uYW1l
IjogImV4YW1wbGVfbW9ja193b3JrZmxvd19vbmUiLCAidGFncyI6IFtdLCAib2JqZWN0X3R5cGUi
OiAiaW5jaWRlbnQiLCAidXVpZCI6IG51bGwsICJhY3Rpb25zIjogW10sICJuYW1lIjogIkV4YW1w
bGU6IE1vY2sgV29ya2Zsb3cgT25lIiwgIndvcmtmbG93X2lkIjogNywgImRlc2NyaXB0aW9uIjog
bnVsbH1dLCAibGFzdF9tb2RpZmllZF90aW1lIjogMTU1ODA4MzE1NzE3OSwgImRlc3RpbmF0aW9u
X2hhbmRsZSI6ICJmbl9tb2NrX2ludGVncmF0aW9uIiwgImlkIjogNDAsICJuYW1lIjogIm1vY2tf
ZnVuY3Rpb25fb25lIn0sIHsiZGlzcGxheV9uYW1lIjogIm1vY2tfZnVuY3Rpb25fdHdvIiwgImRl
c2NyaXB0aW9uIjogeyJjb250ZW50IjogIm1vY2sgZGVzY3JpcHRpb24gdHdvIiwgImZvcm1hdCI6
ICJ0ZXh0In0sICJjcmVhdG9yIjogeyJ0eXBlIjogInVzZXIiLCAiZGlzcGxheV9uYW1lIjogIkFk
bWluIFVzZXIiLCAiaWQiOiA3MSwgIm5hbWUiOiAiYWRtaW5AZXhhbXBsZS5jb20ifSwgInZpZXdf
aXRlbXMiOiBbeyJzaG93X2lmIjogbnVsbCwgImZpZWxkX3R5cGUiOiAiX19mdW5jdGlvbiIsICJz
aG93X2xpbmtfaGVhZGVyIjogZmFsc2UsICJlbGVtZW50IjogImZpZWxkX3V1aWQiLCAiY29udGVu
dCI6ICIxNjkzMzg1Mi03MTJjLTRlM2ItYjc4NS03Yzk5NTE0ZTk1NTEiLCAic3RlcF9sYWJlbCI6
IG51bGx9LCB7InNob3dfaWYiOiBudWxsLCAiZmllbGRfdHlwZSI6ICJfX2Z1bmN0aW9uIiwgInNo
b3dfbGlua19oZWFkZXIiOiBmYWxzZSwgImVsZW1lbnQiOiAiZmllbGRfdXVpZCIsICJjb250ZW50
IjogImExNjEyMjNjLTljNjAtNDgwZi04YjIwLTU5NzQzZTY0ZGQ1MyIsICJzdGVwX2xhYmVsIjog
bnVsbH1dLCAidGFncyI6IFtdLCAiZXhwb3J0X2tleSI6ICJtb2NrX2Z1bmN0aW9uX3R3byIsICJ1
dWlkIjogImQ4NGEzOWI5LTQ3MjYtNDM5MC05Mjk0LTE1MjUxNzRkNDFjYyIsICJsYXN0X21vZGlm
aWVkX2J5IjogeyJ0eXBlIjogInVzZXIiLCAiZGlzcGxheV9uYW1lIjogIkFkbWluIFVzZXIiLCAi
aWQiOiA3MSwgIm5hbWUiOiAiYWRtaW5AZXhhbXBsZS5jb20ifSwgInZlcnNpb24iOiAxLCAid29y
a2Zsb3dzIjogW3sicHJvZ3JhbW1hdGljX25hbWUiOiAiZXhhbXBsZV9tb2NrX3dvcmtmbG93X29u
ZSIsICJ0YWdzIjogW10sICJvYmplY3RfdHlwZSI6ICJpbmNpZGVudCIsICJ1dWlkIjogbnVsbCwg
ImFjdGlvbnMiOiBbXSwgIm5hbWUiOiAiRXhhbXBsZTogTW9jayBXb3JrZmxvdyBPbmUiLCAid29y
a2Zsb3dfaWQiOiA3LCAiZGVzY3JpcHRpb24iOiBudWxsfV0sICJsYXN0X21vZGlmaWVkX3RpbWUi
OiAxNTU4MDgzMTg4NTQ5LCAiZGVzdGluYXRpb25faGFuZGxlIjogImZuX21vY2tfaW50ZWdyYXRp
b24iLCAiaWQiOiA0MSwgIm5hbWUiOiAibW9ja19mdW5jdGlvbl90d28ifV0sICJhY3Rpb25fb3Jk
ZXIiOiBbXSwgImdlb3MiOiBudWxsLCAidGFza19vcmRlciI6IFtdLCAidHlwZXMiOiBbeyJwcm9w
ZXJ0aWVzIjogeyJmb3Jfd2hvIjogW10sICJjYW5fZGVzdHJveSI6IGZhbHNlLCAiY2FuX2NyZWF0
ZSI6IGZhbHNlfSwgImZvcl93b3JrZmxvd3MiOiBmYWxzZSwgImRpc3BsYXlfbmFtZSI6ICJNb2Nr
IERhdGEgVGFibGUiLCAidXVpZCI6ICIyYzg0ZDM5YS04YzJlLTRjNmUtYTlmMC1iNjI5NGJkNGMy
Y2IiLCAidGFncyI6IFtdLCAiZmllbGRzIjogeyJtb2NrX2NvbF8yIjogeyJvcGVyYXRpb25zIjog
W10sICJ0eXBlX2lkIjogMTAwMSwgIm9wZXJhdGlvbl9wZXJtcyI6IHt9LCAidGV4dCI6ICJtb2Nr
IGNvbCAyIiwgImJsYW5rX29wdGlvbiI6IGZhbHNlLCAicHJlZml4IjogbnVsbCwgImNoYW5nZWFi
bGUiOiB0cnVlLCAiaWQiOiAyMzQsICJyZWFkX29ubHkiOiBmYWxzZSwgInV1aWQiOiAiNWNiMjgz
OWItMzhjZi00MTk0LThkNTMtYWQ5YzE5OWY0MjY2IiwgImNob3NlbiI6IGZhbHNlLCAiaW5wdXRf
dHlwZSI6ICJ0ZXh0IiwgInRvb2x0aXAiOiAiIiwgIndpZHRoIjogMzMxLCAiaW50ZXJuYWwiOiBm
YWxzZSwgInJpY2hfdGV4dCI6IGZhbHNlLCAidGVtcGxhdGVzIjogW10sICJ0YWdzIjogW10sICJh
bGxvd19kZWZhdWx0X3ZhbHVlIjogZmFsc2UsICJleHBvcnRfa2V5IjogIm1vY2tfZGF0YV90YWJs
ZS9tb2NrX2NvbF8yIiwgImhpZGVfbm90aWZpY2F0aW9uIjogZmFsc2UsICJwbGFjZWhvbGRlciI6
ICIiLCAiZGVmYXVsdF9jaG9zZW5fYnlfc2VydmVyIjogZmFsc2UsICJuYW1lIjogIm1vY2tfY29s
XzIiLCAiZGVwcmVjYXRlZCI6IGZhbHNlLCAiY2FsY3VsYXRlZCI6IGZhbHNlLCAidmFsdWVzIjog
W10sICJvcmRlciI6IDF9LCAibW9ja19jb2xfMSI6IHsib3BlcmF0aW9ucyI6IFtdLCAidHlwZV9p
ZCI6IDEwMDEsICJvcGVyYXRpb25fcGVybXMiOiB7fSwgInRleHQiOiAibW9jayBjb2wgMSIsICJi
bGFua19vcHRpb24iOiBmYWxzZSwgInByZWZpeCI6IG51bGwsICJjaGFuZ2VhYmxlIjogdHJ1ZSwg
ImlkIjogMjMzLCAicmVhZF9vbmx5IjogZmFsc2UsICJ1dWlkIjogImI1M2FhNmE1LTA0N2YtNDY3
Yi1hNWY3LWMyMjYxYmNkOTEyMSIsICJjaG9zZW4iOiBmYWxzZSwgImlucHV0X3R5cGUiOiAidGV4
dCIsICJ0b29sdGlwIjogIiIsICJ3aWR0aCI6IDMzMCwgImludGVybmFsIjogZmFsc2UsICJyaWNo
X3RleHQiOiBmYWxzZSwgInRlbXBsYXRlcyI6IFtdLCAidGFncyI6IFtdLCAiYWxsb3dfZGVmYXVs
dF92YWx1ZSI6IGZhbHNlLCAiZXhwb3J0X2tleSI6ICJtb2NrX2RhdGFfdGFibGUvbW9ja19jb2xf
MSIsICJoaWRlX25vdGlmaWNhdGlvbiI6IGZhbHNlLCAicGxhY2Vob2xkZXIiOiAiIiwgImRlZmF1
bHRfY2hvc2VuX2J5X3NlcnZlciI6IGZhbHNlLCAibmFtZSI6ICJtb2NrX2NvbF8xIiwgImRlcHJl
Y2F0ZWQiOiBmYWxzZSwgImNhbGN1bGF0ZWQiOiBmYWxzZSwgInZhbHVlcyI6IFtdLCAib3JkZXIi
OiAwfX0sICJwYXJlbnRfdHlwZXMiOiBbImluY2lkZW50Il0sICJ0eXBlX2lkIjogOCwgImV4cG9y
dF9rZXkiOiAibW9ja19kYXRhX3RhYmxlIiwgImZvcl9jdXN0b21fZmllbGRzIjogZmFsc2UsICJh
Y3Rpb25zIjogW10sICJpZCI6IG51bGwsICJmb3JfYWN0aW9ucyI6IGZhbHNlLCAic2NyaXB0cyI6
IFtdLCAidHlwZV9uYW1lIjogIm1vY2tfZGF0YV90YWJsZSIsICJmb3Jfbm90aWZpY2F0aW9ucyI6
IGZhbHNlfV0sICJ0aW1lZnJhbWVzIjogbnVsbCwgIndvcmtzcGFjZXMiOiBbXSwgInRhZ3MiOiBb
XSwgImF1dG9tYXRpY190YXNrcyI6IFtdLCAicGhhc2VzIjogW10sICJub3RpZmljYXRpb25zIjog
bnVsbCwgInJlZ3VsYXRvcnMiOiBudWxsLCAiaW5jaWRlbnRfdHlwZXMiOiBbeyJjcmVhdGVfZGF0
ZSI6IDE1NTgwODM4MDk1MzgsICJkZXNjcmlwdGlvbiI6ICJDdXN0b21pemF0aW9uIFBhY2thZ2Vz
IChpbnRlcm5hbCkiLCAiZXhwb3J0X2tleSI6ICJDdXN0b21pemF0aW9uIFBhY2thZ2VzIChpbnRl
cm5hbCkiLCAiaWQiOiAwLCAibmFtZSI6ICJDdXN0b21pemF0aW9uIFBhY2thZ2VzIChpbnRlcm5h
bCkiLCAidXBkYXRlX2RhdGUiOiAxNTU4MDgzODA5NTM4LCAidXVpZCI6ICJiZmVlYzJkNC0zNzcw
LTExZTgtYWQzOS00YTAwMDQwNDRhYTAiLCAiZW5hYmxlZCI6IGZhbHNlLCAic3lzdGVtIjogZmFs
c2UsICJwYXJlbnRfaWQiOiBudWxsLCAiaGlkZGVuIjogZmFsc2V9XSwgInNjcmlwdHMiOiBbXSwg
InNlcnZlcl92ZXJzaW9uIjogeyJtYWpvciI6IDMzLCAidmVyc2lvbiI6ICIzMy4wLjAiLCAiYnVp
bGRfbnVtYmVyIjogMCwgIm1pbm9yIjogMH0sICJtZXNzYWdlX2Rlc3RpbmF0aW9ucyI6IFt7InBy
b2dyYW1tYXRpY19uYW1lIjogImZuX21vY2tfaW50ZWdyYXRpb24iLCAidGFncyI6IFtdLCAiZXhw
b3J0X2tleSI6ICJmbl9tb2NrX2ludGVncmF0aW9uIiwgInV1aWQiOiAiODE5NTExNzYtYjdjMy00
ZWNkLWJlYWItOGU0ZmUyMzE0MjZiIiwgImV4cGVjdF9hY2siOiB0cnVlLCAiZGVzdGluYXRpb25f
dHlwZSI6IDAsICJ1c2VycyI6IFtdLCAiYXBpX2tleXMiOiBbXSwgIm5hbWUiOiAiZm5fbW9ja19p
bnRlZ3JhdGlvbiJ9XSwgImluY2lkZW50X2FydGlmYWN0X3R5cGVzIjogW10sICJyb2xlcyI6IFtd
LCAiZmllbGRzIjogW3sib3BlcmF0aW9ucyI6IFtdLCAidHlwZV9pZCI6IDExLCAib3BlcmF0aW9u
X3Blcm1zIjoge30sICJ0ZXh0IjogIm1vY2tfZmllbGRfb25lIiwgImJsYW5rX29wdGlvbiI6IGZh
bHNlLCAicHJlZml4IjogbnVsbCwgImNoYW5nZWFibGUiOiB0cnVlLCAiaWQiOiAyMzAsICJyZWFk
X29ubHkiOiBmYWxzZSwgInV1aWQiOiAiMTY5MzM4NTItNzEyYy00ZTNiLWI3ODUtN2M5OTUxNGU5
NTUxIiwgImNob3NlbiI6IGZhbHNlLCAiaW5wdXRfdHlwZSI6ICJ0ZXh0IiwgInRvb2x0aXAiOiAi
bW9ja190b29sdGlwIiwgImludGVybmFsIjogZmFsc2UsICJyaWNoX3RleHQiOiBmYWxzZSwgInRl
bXBsYXRlcyI6IFtdLCAidGFncyI6IFtdLCAiYWxsb3dfZGVmYXVsdF92YWx1ZSI6IGZhbHNlLCAi
ZXhwb3J0X2tleSI6ICJfX2Z1bmN0aW9uL21vY2tfZmllbGRfb25lIiwgImhpZGVfbm90aWZpY2F0
aW9uIjogZmFsc2UsICJwbGFjZWhvbGRlciI6ICJtb2NrX3BsYWNlaG9sZGVyIiwgIm5hbWUiOiAi
bW9ja19maWVsZF9vbmUiLCAiZGVwcmVjYXRlZCI6IGZhbHNlLCAiY2FsY3VsYXRlZCI6IGZhbHNl
LCAicmVxdWlyZWQiOiAiYWx3YXlzIiwgInZhbHVlcyI6IFtdLCAiZGVmYXVsdF9jaG9zZW5fYnlf
c2VydmVyIjogZmFsc2V9LCB7Im9wZXJhdGlvbnMiOiBbXSwgInR5cGVfaWQiOiAxMSwgIm9wZXJh
dGlvbl9wZXJtcyI6IHt9LCAidGV4dCI6ICJtb2NrX2ZpZWxkX3R3byIsICJibGFua19vcHRpb24i
OiBmYWxzZSwgInByZWZpeCI6IG51bGwsICJjaGFuZ2VhYmxlIjogdHJ1ZSwgImlkIjogMjMxLCAi
cmVhZF9vbmx5IjogZmFsc2UsICJ1dWlkIjogImExNjEyMjNjLTljNjAtNDgwZi04YjIwLTU5NzQz
ZTY0ZGQ1MyIsICJjaG9zZW4iOiBmYWxzZSwgImlucHV0X3R5cGUiOiAibnVtYmVyIiwgInRvb2x0
aXAiOiAibW9ja190b29sdGlwX3R3byIsICJpbnRlcm5hbCI6IGZhbHNlLCAicmljaF90ZXh0Ijog
ZmFsc2UsICJ0ZW1wbGF0ZXMiOiBbXSwgInRhZ3MiOiBbXSwgImFsbG93X2RlZmF1bHRfdmFsdWUi
OiBmYWxzZSwgImV4cG9ydF9rZXkiOiAiX19mdW5jdGlvbi9tb2NrX2ZpZWxkX3R3byIsICJoaWRl
X25vdGlmaWNhdGlvbiI6IGZhbHNlLCAicGxhY2Vob2xkZXIiOiAibW9ja19wbGFjZWhvbGRlcl90
d28iLCAibmFtZSI6ICJtb2NrX2ZpZWxkX3R3byIsICJkZXByZWNhdGVkIjogZmFsc2UsICJjYWxj
dWxhdGVkIjogZmFsc2UsICJyZXF1aXJlZCI6ICJhbHdheXMiLCAidmFsdWVzIjogW10sICJkZWZh
dWx0X2Nob3Nlbl9ieV9zZXJ2ZXIiOiBmYWxzZX0sIHsib3BlcmF0aW9ucyI6IFtdLCAidHlwZV9p
ZCI6IDYsICJvcGVyYXRpb25fcGVybXMiOiB7fSwgInRleHQiOiAiTW9jayBBY3Rpdml0eSBGaWVs
ZCBPbmUiLCAiYmxhbmtfb3B0aW9uIjogZmFsc2UsICJwcmVmaXgiOiAicHJvcGVydGllcyIsICJj
aGFuZ2VhYmxlIjogdHJ1ZSwgImlkIjogMjMyLCAicmVhZF9vbmx5IjogZmFsc2UsICJ1dWlkIjog
ImYxZDU0MTlmLWRiODktNGI2Yy1hN2YwLTEwNTU5YTZlMzZjMiIsICJjaG9zZW4iOiBmYWxzZSwg
ImlucHV0X3R5cGUiOiAidGV4dCIsICJ0b29sdGlwIjogIiIsICJpbnRlcm5hbCI6IGZhbHNlLCAi
cmljaF90ZXh0IjogZmFsc2UsICJ0ZW1wbGF0ZXMiOiBbXSwgInRhZ3MiOiBbXSwgImFsbG93X2Rl
ZmF1bHRfdmFsdWUiOiBmYWxzZSwgImV4cG9ydF9rZXkiOiAiYWN0aW9uaW52b2NhdGlvbi9tb2Nr
X2FjdGl2aXR5X2ZpZWxkX29uZSIsICJoaWRlX25vdGlmaWNhdGlvbiI6IGZhbHNlLCAicGxhY2Vo
b2xkZXIiOiAibW9jayBwbGFjZWhvbGRlciIsICJuYW1lIjogIm1vY2tfYWN0aXZpdHlfZmllbGRf
b25lIiwgImRlcHJlY2F0ZWQiOiBmYWxzZSwgImNhbGN1bGF0ZWQiOiBmYWxzZSwgInZhbHVlcyI6
IFtdLCAiZGVmYXVsdF9jaG9zZW5fYnlfc2VydmVyIjogZmFsc2V9LCB7Im9wZXJhdGlvbnMiOiBb
XSwgInR5cGVfaWQiOiAwLCAib3BlcmF0aW9uX3Blcm1zIjoge30sICJ0ZXh0IjogIm1vY2sgaW5j
aWRlbnQgZmllbGQiLCAiYmxhbmtfb3B0aW9uIjogZmFsc2UsICJwcmVmaXgiOiAicHJvcGVydGll
cyIsICJjaGFuZ2VhYmxlIjogdHJ1ZSwgImlkIjogMjM1LCAicmVhZF9vbmx5IjogZmFsc2UsICJ1
dWlkIjogImY5MGI4Mzg2LTJmZDUtNDg2Ny05ZmM4LWY1MjM4ZWYzYjZmYyIsICJjaG9zZW4iOiBm
YWxzZSwgImlucHV0X3R5cGUiOiAidGV4dCIsICJ0b29sdGlwIjogIiIsICJpbnRlcm5hbCI6IGZh
bHNlLCAicmljaF90ZXh0IjogZmFsc2UsICJ0ZW1wbGF0ZXMiOiBbXSwgInRhZ3MiOiBbXSwgImFs
bG93X2RlZmF1bHRfdmFsdWUiOiBmYWxzZSwgImV4cG9ydF9rZXkiOiAiaW5jaWRlbnQvbW9ja19p
bmNpZGVudF9maWVsZCIsICJoaWRlX25vdGlmaWNhdGlvbiI6IGZhbHNlLCAicGxhY2Vob2xkZXIi
OiAiIiwgIm5hbWUiOiAibW9ja19pbmNpZGVudF9maWVsZCIsICJkZXByZWNhdGVkIjogZmFsc2Us
ICJjYWxjdWxhdGVkIjogZmFsc2UsICJ2YWx1ZXMiOiBbXSwgImRlZmF1bHRfY2hvc2VuX2J5X3Nl
cnZlciI6IGZhbHNlfV0sICJvdmVycmlkZXMiOiBbXSwgImV4cG9ydF9kYXRlIjogMTU1ODA4Mzgw
ODAyOX0=
"""
    )