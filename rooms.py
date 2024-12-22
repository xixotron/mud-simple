#vim: set fileencoding=utf-8

rooms = {
    "casa": {
        "description": "Estas en una sucia casa.",
        "exits": {"fuera": "fuera"},
    },
    "fuera": {
        "description": "Estas fuera de una casa. Esta lloviendo.",
        "exits": {"dentro": "casa"},
    }
}
