STATE_REQUEST_KEY = "session"
STATE_RESPONSE_KEY = "session_state"
USERSTATE_RESPONSE_KEY = "user_state_update"
PREVIOUS_MOVES = "prev_moves"

# region State of dialog

STUDENTS = "students"

# endregion

# help menu
PREVIOUS_STATE = "previous_state"
NEXT_BUTTON = "next_button"

# Эти состояния будут сохранены в fallback
MUST_BE_SAVE = {PREVIOUS_STATE, NEXT_BUTTON}

# Эти состояния сохраняются на каждый ход
PERMANENT_VALUES = {}
