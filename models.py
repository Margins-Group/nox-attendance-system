# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
# Unable to inspect table 'AccessRings'
# The error was: ('42000', "[42000] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]The SELECT permission was denied on the object 'columns', database 'mssqlsystemresource', schema 'sys'. (229) (SQLExecDirectW)")
# Unable to inspect table 'AccessRingsUsers'
# The error was: ('42000', "[42000] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]The SELECT permission was denied on the object 'columns', database 'mssqlsystemresource', schema 'sys'. (229) (SQLExecDirectW)")
# Unable to inspect table 'AddOn'
# The error was: ('42000', "[42000] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]The SELECT permission was denied on the object 'columns', database 'mssqlsystemresource', schema 'sys'. (229) (SQLExecDirectW)")
# Unable to inspect table 'AlarmCallConfig'
# The error was: ('42000', "[42000] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]The SELECT permission was denied on the object 'columns', database 'mssqlsystemresource', schema 'sys'. (229) (SQLExecDirectW)")
# Unable to inspect table 'AlarmCallGroups'
# The error was: ('42000', "[42000] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]The SELECT permission was denied on the object 'columns', database 'mssqlsystemresource', schema 'sys'. (229) (SQLExecDirectW)")
# Unable to inspect table 'AlarmCallGroupsKW'
# The error was: ('42000', "[42000] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]The SELECT permission was denied on the object 'columns', database 'mssqlsystemresource', schema 'sys'. (229) (SQLExecDirectW)")
# Unable to inspect table 'AlarmCallGroupsKWtimes'
# The error was: ('42000', "[42000] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]The SELECT permission was denied on the object 'columns', database 'mssqlsystemresource', schema 'sys'. (229) (SQLExecDirectW)")
# Unable to inspect table 'AlarmCallTexts'
# The error was: ('42000', "[42000] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]The SELECT permission was denied on the object 'columns', database 'mssqlsystemresource', schema 'sys'. (229) (SQLExecDirectW)")
# Unable to inspect table 'AlarmCallUsers'
# The error was: ('42000', "[42000] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]The SELECT permission was denied on the object 'columns', database 'mssqlsystemresource', schema 'sys'. (229) (SQLExecDirectW)")
# Unable to inspect table 'AlarmIntervention'
# The error was: ('42000', "[42000] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]The SELECT permission was denied on the object 'columns', database 'mssqlsystemresource', schema 'sys'. (229) (SQLExecDirectW)")
# Unable to inspect table 'AlarmInterventionEdit'
# The error was: ('42000', "[42000] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]The SELECT permission was denied on the object 'columns', database 'mssqlsystemresource', schema 'sys'. (229) (SQLExecDirectW)")
# Unable to inspect table 'AlarmReason'
# The error was: ('42000', "[42000] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]The SELECT permission was denied on the object 'columns', database 'mssqlsystemresource', schema 'sys'. (229) (SQLExecDirectW)")
# Unable to inspect table 'AlarmTelephone'
# The error was: ('42000', "[42000] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]The SELECT permission was denied on the object 'columns', database 'mssqlsystemresource', schema 'sys'. (229) (SQLExecDirectW)")
# Unable to inspect table 'AlarmType'
# The error was: ('42000', "[42000] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]The SELECT permission was denied on the object 'columns', database 'mssqlsystemresource', schema 'sys'. (229) (SQLExecDirectW)")
# Unable to inspect table 'AreaStateColors'
# The error was: ('42000', "[42000] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]The SELECT permission was denied on the object 'columns', database 'mssqlsystemresource', schema 'sys'. (229) (SQLExecDirectW)")
# Unable to inspect table 'Areas'
# The error was: ('42000', "[42000] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]The SELECT permission was denied on the object 'columns', database 'mssqlsystemresource', schema 'sys'. (229) (SQLExecDirectW)")
# Unable to inspect table 'Avigilon'
# The error was: ('42000', "[42000] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]The SELECT permission was denied on the object 'columns', database 'mssqlsystemresource', schema 'sys'. (229) (SQLExecDirectW)")
# Unable to inspect table 'Clients'
# The error was: ('42000', "[42000] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]The SELECT permission was denied on the object 'columns', database 'mssqlsystemresource', schema 'sys'. (229) (SQLExecDirectW)")
# Unable to inspect table 'Commands'
# The error was: ('42000', "[42000] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]The SELECT permission was denied on the object 'columns', database 'mssqlsystemresource', schema 'sys'. (229) (SQLExecDirectW)")
# Unable to inspect table 'Config'
# The error was: ('42000', "[42000] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]The SELECT permission was denied on the object 'columns', database 'mssqlsystemresource', schema 'sys'. (229) (SQLExecDirectW)")
# Unable to inspect table 'Counters'
# The error was: ('42000', "[42000] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]The SELECT permission was denied on the object 'columns', database 'mssqlsystemresource', schema 'sys'. (229) (SQLExecDirectW)")
# Unable to inspect table 'CountersUsers'
# The error was: ('42000', "[42000] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]The SELECT permission was denied on the object 'columns', database 'mssqlsystemresource', schema 'sys'. (229) (SQLExecDirectW)")
# Unable to inspect table 'DVRviews'
# The error was: ('42000', "[42000] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]The SELECT permission was denied on the object 'columns', database 'mssqlsystemresource', schema 'sys'. (229) (SQLExecDirectW)")
# Unable to inspect table 'Holidays'
# The error was: ('42000', "[42000] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]The SELECT permission was denied on the object 'columns', database 'mssqlsystemresource', schema 'sys'. (229) (SQLExecDirectW)")
# Unable to inspect table 'INEX'
# The error was: ('42000', "[42000] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]The SELECT permission was denied on the object 'columns', database 'mssqlsystemresource', schema 'sys'. (229) (SQLExecDirectW)")
# Unable to inspect table 'InputSymbols'
# The error was: ('42000', "[42000] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]The SELECT permission was denied on the object 'columns', database 'mssqlsystemresource', schema 'sys'. (229) (SQLExecDirectW)")
# Unable to inspect table 'InputTypes'
# The error was: ('42000', "[42000] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]The SELECT permission was denied on the object 'columns', database 'mssqlsystemresource', schema 'sys'. (229) (SQLExecDirectW)")
# Unable to inspect table 'Inputs'
# The error was: ('42000', "[42000] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]The SELECT permission was denied on the object 'columns', database 'mssqlsystemresource', schema 'sys'. (229) (SQLExecDirectW)")
# Unable to inspect table 'Level'
# The error was: ('42000', "[42000] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]The SELECT permission was denied on the object 'columns', database 'mssqlsystemresource', schema 'sys'. (229) (SQLExecDirectW)")
# Unable to inspect table 'LevelSIMS'
# The error was: ('42000', "[42000] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]The SELECT permission was denied on the object 'columns', database 'mssqlsystemresource', schema 'sys'. (229) (SQLExecDirectW)")
# Unable to inspect table 'LogAlarm'
# The error was: ('42000', "[42000] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]The SELECT permission was denied on the object 'columns', database 'mssqlsystemresource', schema 'sys'. (229) (SQLExecDirectW)")
# Unable to inspect table 'LogAlarmCall'
# The error was: ('42000', "[42000] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]The SELECT permission was denied on the object 'columns', database 'mssqlsystemresource', schema 'sys'. (229) (SQLExecDirectW)")
# Unable to inspect table 'LogDiagnostic'
# The error was: ('42000', "[42000] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]The SELECT permission was denied on the object 'columns', database 'mssqlsystemresource', schema 'sys'. (229) (SQLExecDirectW)")
# Unable to inspect table 'LogInputStateChanges'
# The error was: ('42000', "[42000] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]The SELECT permission was denied on the object 'columns', database 'mssqlsystemresource', schema 'sys'. (229) (SQLExecDirectW)")
# Unable to inspect table 'LogSystems'
# The error was: ('42000', "[42000] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]The SELECT permission was denied on the object 'columns', database 'mssqlsystemresource', schema 'sys'. (229) (SQLExecDirectW)")
# Unable to inspect table 'LogSystemsAreaStates'
# The error was: ('42000', "[42000] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]The SELECT permission was denied on the object 'columns', database 'mssqlsystemresource', schema 'sys'. (229) (SQLExecDirectW)")
# Unable to inspect table 'LogSystemsAreas'
# The error was: ('42000', "[42000] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]The SELECT permission was denied on the object 'columns', database 'mssqlsystemresource', schema 'sys'. (229) (SQLExecDirectW)")
# Unable to inspect table 'LogSystemsUsers'
# The error was: ('42000', "[42000] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]The SELECT permission was denied on the object 'columns', database 'mssqlsystemresource', schema 'sys'. (229) (SQLExecDirectW)")
# Unable to inspect table 'LogTHS'
# The error was: ('42000', "[42000] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]The SELECT permission was denied on the object 'columns', database 'mssqlsystemresource', schema 'sys'. (229) (SQLExecDirectW)")
# Unable to inspect table 'LogTerminal'
# The error was: ('42000', "[42000] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]The SELECT permission was denied on the object 'columns', database 'mssqlsystemresource', schema 'sys'. (229) (SQLExecDirectW)")
# Unable to inspect table 'LogUsers'
# The error was: ('42000', "[42000] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]The SELECT permission was denied on the object 'columns', database 'mssqlsystemresource', schema 'sys'. (229) (SQLExecDirectW)")
# Unable to inspect table 'Maps'
# The error was: ('42000', "[42000] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]The SELECT permission was denied on the object 'columns', database 'mssqlsystemresource', schema 'sys'. (229) (SQLExecDirectW)")
# Unable to inspect table 'Milestone'
# The error was: ('42000', "[42000] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]The SELECT permission was denied on the object 'columns', database 'mssqlsystemresource', schema 'sys'. (229) (SQLExecDirectW)")
# Unable to inspect table 'MilestoneVideoClients'
# The error was: ('42000', "[42000] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]The SELECT permission was denied on the object 'columns', database 'mssqlsystemresource', schema 'sys'. (229) (SQLExecDirectW)")
# Unable to inspect table 'MonitorSwitch'
# The error was: ('42000', "[42000] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]The SELECT permission was denied on the object 'columns', database 'mssqlsystemresource', schema 'sys'. (229) (SQLExecDirectW)")
# Unable to inspect table 'Monitors'
# The error was: ('42000', "[42000] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]The SELECT permission was denied on the object 'columns', database 'mssqlsystemresource', schema 'sys'. (229) (SQLExecDirectW)")
# Unable to inspect table 'NoxAreaGroups'
# The error was: ('42000', "[42000] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]The SELECT permission was denied on the object 'columns', database 'mssqlsystemresource', schema 'sys'. (229) (SQLExecDirectW)")
# Unable to inspect table 'NoxUnits'
# The error was: ('42000', "[42000] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]The SELECT permission was denied on the object 'columns', database 'mssqlsystemresource', schema 'sys'. (229) (SQLExecDirectW)")
# Unable to inspect table 'Outputs'
# The error was: ('42000', "[42000] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]The SELECT permission was denied on the object 'columns', database 'mssqlsystemresource', schema 'sys'. (229) (SQLExecDirectW)")
# Unable to inspect table 'PresentList'
# The error was: ('42000', "[42000] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]The SELECT permission was denied on the object 'columns', database 'mssqlsystemresource', schema 'sys'. (229) (SQLExecDirectW)")
# Unable to inspect table 'PrinterSettings'
# The error was: ('42000', "[42000] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]The SELECT permission was denied on the object 'columns', database 'mssqlsystemresource', schema 'sys'. (229) (SQLExecDirectW)")
# Unable to inspect table 'SIMScodesAreaGroups'
# The error was: ('42000', "[42000] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]The SELECT permission was denied on the object 'columns', database 'mssqlsystemresource', schema 'sys'. (229) (SQLExecDirectW)")
# Unable to inspect table 'SIMScodesAutoUpdate'
# The error was: ('42000', "[42000] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]The SELECT permission was denied on the object 'columns', database 'mssqlsystemresource', schema 'sys'. (229) (SQLExecDirectW)")
# Unable to inspect table 'SIMScodesAutoUpdateLog'
# The error was: ('42000', "[42000] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]The SELECT permission was denied on the object 'columns', database 'mssqlsystemresource', schema 'sys'. (229) (SQLExecDirectW)")
# Unable to inspect table 'SIMScodesNoxUserProfiles'
# The error was: ('42000', "[42000] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]The SELECT permission was denied on the object 'columns', database 'mssqlsystemresource', schema 'sys'. (229) (SQLExecDirectW)")
# Unable to inspect table 'SIMScodesNoxUserProfilesBak'
# The error was: ('42000', "[42000] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]The SELECT permission was denied on the object 'columns', database 'mssqlsystemresource', schema 'sys'. (229) (SQLExecDirectW)")
# Unable to inspect table 'SIMScodesNoxUserprofilesX'
# The error was: ('42000', "[42000] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]The SELECT permission was denied on the object 'columns', database 'mssqlsystemresource', schema 'sys'. (229) (SQLExecDirectW)")
# Unable to inspect table 'SIMScodesUP'
# The error was: ('42000', "[42000] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]The SELECT permission was denied on the object 'columns', database 'mssqlsystemresource', schema 'sys'. (229) (SQLExecDirectW)")
# Unable to inspect table 'SIMScodesUsers'
# The error was: ('42000', "[42000] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]The SELECT permission was denied on the object 'columns', database 'mssqlsystemresource', schema 'sys'. (229) (SQLExecDirectW)")
# Unable to inspect table 'SIMScodesUsersAdditionalFields'
# The error was: ('42000', "[42000] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]The SELECT permission was denied on the object 'columns', database 'mssqlsystemresource', schema 'sys'. (229) (SQLExecDirectW)")
# Unable to inspect table 'SIMScodesUsersAdditionalFieldsDefs'
# The error was: ('42000', "[42000] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]The SELECT permission was denied on the object 'columns', database 'mssqlsystemresource', schema 'sys'. (229) (SQLExecDirectW)")
# Unable to inspect table 'SIMScodesUsersBak'
# The error was: ('42000', "[42000] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]The SELECT permission was denied on the object 'columns', database 'mssqlsystemresource', schema 'sys'. (229) (SQLExecDirectW)")
# Unable to inspect table 'Systems'
# The error was: ('42000', "[42000] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]The SELECT permission was denied on the object 'columns', database 'mssqlsystemresource', schema 'sys'. (229) (SQLExecDirectW)")
# Unable to inspect table 'UserActivity'
# The error was: ('42000', "[42000] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]The SELECT permission was denied on the object 'columns', database 'mssqlsystemresource', schema 'sys'. (229) (SQLExecDirectW)")
# Unable to inspect table 'Users'
# The error was: ('42000', "[42000] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]The SELECT permission was denied on the object 'columns', database 'mssqlsystemresource', schema 'sys'. (229) (SQLExecDirectW)")
# Unable to inspect table 'VCR'
# The error was: ('42000', "[42000] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]The SELECT permission was denied on the object 'columns', database 'mssqlsystemresource', schema 'sys'. (229) (SQLExecDirectW)")
# Unable to inspect table 'dtproperties'
# The error was: ('42000', "[42000] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]The SELECT permission was denied on the object 'columns', database 'mssqlsystemresource', schema 'sys'. (229) (SQLExecDirectW)")
# Unable to inspect table 'sysdiagrams'
# The error was: ('42000', "[42000] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]The SELECT permission was denied on the object 'columns', database 'mssqlsystemresource', schema 'sys'. (229) (SQLExecDirectW)")
