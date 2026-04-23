# AUTO-GENERATED — DO NOT EDIT
# source-sha256: 9fd85db769ef2b21bf5e0029cc36b894e720c0e5b7d80de6a385a0bbb9555cff
# Run tools/update_ns.py to regenerate.
from __future__ import annotations

_URI: str = "http://opcfoundation.org/UA/Scheduler/"
_VERSION: str = "1.05.02"
_REQUIRED: list = [{"uri": "http://opcfoundation.org/UA/", "version": ""}]
_STRUCTURES: list = [
    (
        "ns=1;i=70",
        "SpecialEventType",
        "ns=1;i=87",
        {
            "structure_type": 0,
            "fields": [
                {"name": "Period", "data_type": "ns=1;i=71", "value_rank": -1},
                {
                    "name": "ListOfTimeActions",
                    "data_type": "ns=1;i=81",
                    "value_rank": 1,
                },
                {"name": "EventPriority", "data_type": "i=3", "value_rank": -1},
            ],
        },
    ),
    (
        "ns=1;i=71",
        "SpecialEventPeriodType",
        "ns=1;i=88",
        {
            "structure_type": 0,
            "fields": [
                {"name": "CalendarEntry", "data_type": "ns=1;i=72", "value_rank": -1},
                {"name": "CalendarReference", "data_type": "i=17", "value_rank": -1},
            ],
        },
    ),
    (
        "ns=1;i=72",
        "CalendarEntryType",
        "ns=1;i=89",
        {
            "structure_type": 0,
            "fields": [
                {"name": "Date", "data_type": "ns=1;i=73", "value_rank": -1},
                {"name": "DateRange", "data_type": "ns=1;i=80", "value_rank": -1},
            ],
        },
    ),
    (
        "ns=1;i=73",
        "DateType",
        "ns=1;i=90",
        {
            "structure_type": 0,
            "fields": [
                {"name": "Year", "data_type": "i=5", "value_rank": -1},
                {"name": "Month", "data_type": "ns=1;i=74", "value_rank": -1},
                {"name": "DayOfMonth", "data_type": "ns=1;i=76", "value_rank": -1},
                {"name": "DayOfWeek", "data_type": "ns=1;i=78", "value_rank": -1},
            ],
        },
    ),
    (
        "ns=1;i=80",
        "DateRangeType",
        "ns=1;i=91",
        {
            "structure_type": 0,
            "fields": [
                {"name": "StartDate", "data_type": "ns=1;i=73", "value_rank": -1},
                {"name": "EndDate", "data_type": "ns=1;i=73", "value_rank": -1},
            ],
        },
    ),
    (
        "ns=1;i=81",
        "TimeActionsType",
        "ns=1;i=92",
        {
            "structure_type": 0,
            "fields": [
                {"name": "Time", "data_type": "ns=1;i=85", "value_rank": -1},
                {"name": "Actions", "data_type": "ns=1;i=82", "value_rank": 1},
            ],
        },
    ),
    (
        "ns=1;i=82",
        "BaseActionType",
        "ns=1;i=93",
        {
            "structure_type": 0,
            "fields": [
                {"name": "LastActionResult", "data_type": "i=19", "value_rank": -1}
            ],
        },
    ),
    (
        "ns=1;i=83",
        "WriteLocalVariableActionType",
        "ns=1;i=94",
        {
            "structure_type": 0,
            "fields": [
                {"name": "Variable", "data_type": "i=17", "value_rank": -1},
                {"name": "Value", "data_type": "i=24", "value_rank": -1},
            ],
        },
    ),
    (
        "ns=1;i=84",
        "CallLocalMethodActionType",
        "ns=1;i=95",
        {
            "structure_type": 0,
            "fields": [
                {"name": "ObjectId", "data_type": "i=17", "value_rank": -1},
                {"name": "MethodId", "data_type": "i=17", "value_rank": -1},
                {"name": "InputValues", "data_type": "i=24", "value_rank": 1},
                {"name": "LastOutputValues", "data_type": "i=24", "value_rank": 1},
            ],
        },
    ),
    (
        "ns=1;i=85",
        "TimeType",
        "ns=1;i=96",
        {
            "structure_type": 0,
            "fields": [
                {"name": "Hour", "data_type": "i=3", "value_rank": -1},
                {"name": "Minute", "data_type": "i=3", "value_rank": -1},
                {"name": "Second", "data_type": "i=3", "value_rank": -1},
            ],
        },
    ),
    (
        "ns=1;i=86",
        "DailyScheduleType",
        "ns=1;i=97",
        {
            "structure_type": 0,
            "fields": [
                {"name": "DaySchedule", "data_type": "ns=1;i=81", "value_rank": 1}
            ],
        },
    ),
]
_ENUMS: list = [
    (
        "ns=1;i=74",
        "Month",
        {
            "fields": [
                {"name": "Unspecified", "value": 0, "display_name": "Unspecified"},
                {"name": "January", "value": 1, "display_name": "January"},
                {"name": "February", "value": 2, "display_name": "February"},
                {"name": "March", "value": 3, "display_name": "March"},
                {"name": "April", "value": 4, "display_name": "April"},
                {"name": "May", "value": 5, "display_name": "May"},
                {"name": "June", "value": 6, "display_name": "June"},
                {"name": "July", "value": 7, "display_name": "July"},
                {"name": "August", "value": 8, "display_name": "August"},
                {"name": "September", "value": 9, "display_name": "September"},
                {"name": "October", "value": 10, "display_name": "October"},
                {"name": "November", "value": 11, "display_name": "November"},
                {"name": "December", "value": 12, "display_name": "December"},
                {"name": "Odd", "value": 13, "display_name": "Odd"},
                {"name": "Even", "value": 14, "display_name": "Even"},
            ]
        },
    ),
    (
        "ns=1;i=76",
        "DayOfMonth",
        {
            "fields": [
                {"name": "Unspecified", "value": 0, "display_name": "Unspecified"},
                {"name": "Day1", "value": 1, "display_name": "Day1"},
                {"name": "Day2", "value": 2, "display_name": "Day2"},
                {"name": "Day3", "value": 3, "display_name": "Day3"},
                {"name": "Day4", "value": 4, "display_name": "Day4"},
                {"name": "Day5", "value": 5, "display_name": "Day5"},
                {"name": "Day6", "value": 6, "display_name": "Day6"},
                {"name": "Day7", "value": 7, "display_name": "Day7"},
                {"name": "Day8", "value": 8, "display_name": "Day8"},
                {"name": "Day9", "value": 9, "display_name": "Day9"},
                {"name": "Day10", "value": 10, "display_name": "Day10"},
                {"name": "Day11", "value": 11, "display_name": "Day11"},
                {"name": "Day12", "value": 12, "display_name": "Day12"},
                {"name": "Day13", "value": 13, "display_name": "Day13"},
                {"name": "Day14", "value": 14, "display_name": "Day14"},
                {"name": "Day15", "value": 15, "display_name": "Day15"},
                {"name": "Day16", "value": 16, "display_name": "Day16"},
                {"name": "Day17", "value": 17, "display_name": "Day17"},
                {"name": "Day18", "value": 18, "display_name": "Day18"},
                {"name": "Day19", "value": 19, "display_name": "Day19"},
                {"name": "Day20", "value": 20, "display_name": "Day20"},
                {"name": "Day21", "value": 21, "display_name": "Day21"},
                {"name": "Day22", "value": 22, "display_name": "Day22"},
                {"name": "Day23", "value": 23, "display_name": "Day23"},
                {"name": "Day24", "value": 24, "display_name": "Day24"},
                {"name": "Day25", "value": 25, "display_name": "Day25"},
                {"name": "Day26", "value": 26, "display_name": "Day26"},
                {"name": "Day27", "value": 27, "display_name": "Day27"},
                {"name": "Day28", "value": 28, "display_name": "Day28"},
                {"name": "Day29", "value": 29, "display_name": "Day29"},
                {"name": "Day30", "value": 30, "display_name": "Day30"},
                {"name": "Day31", "value": 31, "display_name": "Day31"},
                {
                    "name": "LastDayOfMonth",
                    "value": 32,
                    "display_name": "LastDayOfMonth",
                },
                {"name": "OddDayOfMonth", "value": 33, "display_name": "OddDayOfMonth"},
                {
                    "name": "EvenDayOfMonth",
                    "value": 34,
                    "display_name": "EvenDayOfMonth",
                },
            ]
        },
    ),
    (
        "ns=1;i=78",
        "DayOfWeek",
        {
            "fields": [
                {"name": "Unspecified", "value": 0, "display_name": "Unspecified"},
                {"name": "Monday", "value": 1, "display_name": "Monday"},
                {"name": "Tuesday", "value": 2, "display_name": "Tuesday"},
                {"name": "Wednesday", "value": 3, "display_name": "Wednesday"},
                {"name": "Thursday", "value": 4, "display_name": "Thursday"},
                {"name": "Friday", "value": 5, "display_name": "Friday"},
                {"name": "Saturday", "value": 6, "display_name": "Saturday"},
                {"name": "Sunday", "value": 7, "display_name": "Sunday"},
            ]
        },
    ),
]
_ORIGINAL_NODEIDS: tuple = (
    [
        ("ns=1;i=70", "ns=1;i=87", ["ns=1;i=71", "ns=1;i=81", "i=3"]),
        ("ns=1;i=71", "ns=1;i=88", ["ns=1;i=72", "i=17"]),
        ("ns=1;i=72", "ns=1;i=89", ["ns=1;i=73", "ns=1;i=80"]),
        ("ns=1;i=73", "ns=1;i=90", ["i=5", "ns=1;i=74", "ns=1;i=76", "ns=1;i=78"]),
        ("ns=1;i=80", "ns=1;i=91", ["ns=1;i=73", "ns=1;i=73"]),
        ("ns=1;i=81", "ns=1;i=92", ["ns=1;i=85", "ns=1;i=82"]),
        ("ns=1;i=82", "ns=1;i=93", ["i=19"]),
        ("ns=1;i=83", "ns=1;i=94", ["i=17", "i=24"]),
        ("ns=1;i=84", "ns=1;i=95", ["i=17", "i=17", "i=24", "i=24"]),
        ("ns=1;i=85", "ns=1;i=96", ["i=3", "i=3", "i=3"]),
        ("ns=1;i=86", "ns=1;i=97", ["ns=1;i=81"]),
    ],
    ["ns=1;i=74", "ns=1;i=76", "ns=1;i=78"],
)
_NODES: dict = {
    "datatypes": {
        "BaseActionType": (
            "D",
            "ns=1;i=82",
            {
                "CallLocalMethodActionType": ("D", "ns=1;i=84", {}),
                "WriteLocalVariableActionType": ("D", "ns=1;i=83", {}),
            },
        ),
        "CalendarEntryType": ("D", "ns=1;i=72", {}),
        "DailyScheduleType": ("D", "ns=1;i=86", {}),
        "DateRangeType": ("D", "ns=1;i=80", {}),
        "DateType": ("D", "ns=1;i=73", {}),
        "DayOfMonth": ("D", "ns=1;i=76", {"EnumStrings": ("V", "ns=1;i=195", {})}),
        "DayOfWeek": ("D", "ns=1;i=78", {"EnumStrings": ("V", "ns=1;i=79", {})}),
        "Month": ("D", "ns=1;i=74", {"EnumStrings": ("V", "ns=1;i=194", {})}),
        "SpecialEventPeriodType": ("D", "ns=1;i=71", {}),
        "SpecialEventType": ("D", "ns=1;i=70", {}),
        "TimeActionsType": ("D", "ns=1;i=81", {}),
        "TimeType": ("D", "ns=1;i=85", {}),
    },
    "objects": {
        "Default Binary": ("O", "ns=1;i=97", {}),
        "Default JSON": ("O", "ns=1;i=193", {}),
        "Default XML": ("O", "ns=1;i=145", {}),
        "Opc.Ua.Scheduler": (
            "V",
            "ns=1;i=146",
            {
                "BaseActionType": ("V", "ns=1;i=168", {}),
                "CalendarEntryType": ("V", "ns=1;i=156", {}),
                "CallLocalMethodActionType": ("V", "ns=1;i=174", {}),
                "DailyScheduleType": ("V", "ns=1;i=180", {}),
                "DateRangeType": ("V", "ns=1;i=162", {}),
                "DateType": ("V", "ns=1;i=159", {}),
                "Deprecated": ("V", "ns=1;i=149", {}),
                "NamespaceUri": ("V", "ns=1;i=148", {}),
                "SpecialEventPeriodType": ("V", "ns=1;i=153", {}),
                "SpecialEventType": ("V", "ns=1;i=150", {}),
                "TimeActionsType": ("V", "ns=1;i=165", {}),
                "TimeType": ("V", "ns=1;i=177", {}),
                "WriteLocalVariableActionType": ("V", "ns=1;i=171", {}),
            },
        ),
        "http://opcfoundation.org/UA/Scheduler/": (
            "O",
            "ns=1;i=1",
            {
                "DefaultAccessRestrictions": ("V", "ns=1;i=35", {}),
                "DefaultRolePermissions": ("V", "ns=1;i=33", {}),
                "DefaultUserRolePermissions": ("V", "ns=1;i=34", {}),
                "IsNamespaceSubset": ("V", "ns=1;i=5", {}),
                "NamespacePublicationDate": ("V", "ns=1;i=4", {}),
                "NamespaceUri": ("V", "ns=1;i=2", {}),
                "NamespaceVersion": ("V", "ns=1;i=3", {}),
                "StaticNodeIdTypes": ("V", "ns=1;i=6", {}),
                "StaticNumericNodeIdRange": ("V", "ns=1;i=7", {}),
                "StaticStringNodeIdPattern": ("V", "ns=1;i=8", {}),
            },
        ),
    },
    "objtypes": {
        "CalendarType": (
            "OT",
            "ns=1;i=37",
            {
                "AddDateListElements": (
                    "M",
                    "ns=1;i=40",
                    {
                        "InputArguments": ("V", "ns=1;i=41", {}),
                        "OutputArguments": ("V", "ns=1;i=42", {}),
                    },
                ),
                "DateList": ("V", "ns=1;i=39", {}),
                "PresentValue": ("V", "ns=1;i=38", {}),
                "RemoveDateListElements": (
                    "M",
                    "ns=1;i=43",
                    {
                        "InputArguments": ("V", "ns=1;i=44", {}),
                        "OutputArguments": ("V", "ns=1;i=45", {}),
                    },
                ),
            },
        ),
        "ScheduleType": (
            "OT",
            "ns=1;i=52",
            {
                "AddExceptionScheduleElements": (
                    "M",
                    "ns=1;i=54",
                    {
                        "InputArguments": ("V", "ns=1;i=55", {}),
                        "OutputArguments": ("V", "ns=1;i=56", {}),
                    },
                ),
                "ApplyLastAfterStart": ("V", "ns=1;i=63", {}),
                "EffectivePeriod": ("V", "ns=1;i=62", {}),
                "ExceptionSchedule": ("V", "ns=1;i=53", {}),
                "LocalTime": ("V", "ns=1;i=61", {}),
                "RemoveExceptionScheduleElements": (
                    "M",
                    "ns=1;i=57",
                    {
                        "InputArguments": ("V", "ns=1;i=58", {}),
                        "OutputArguments": ("V", "ns=1;i=59", {}),
                    },
                ),
                "WeeklySchedule": ("V", "ns=1;i=60", {}),
            },
        ),
    },
}
