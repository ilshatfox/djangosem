from vk_bot.base.enums import BaseEnum


class TaskType(BaseEnum):
    ADD_FRIEND = 'ADD_FRIEND'
    # ADD_FRIEND = 'https'

    values = {
        ADD_FRIEND: 'ADD_FRIEND',
        # HTTPS: 'https'
    }


class FollowTaskStatusType(BaseEnum):
    NEW = 'NEW'
    READY_TO_START = 'READY_TO_START'
    ACTIVE = 'ACTIVE'
    COMPLETE = 'COMPLETE'

    values = {
        NEW: 'NEW',
        READY_TO_START: 'READY_TO_START',
        ACTIVE: 'ACTIVE',
        COMPLETE: 'COMPLETE'
    }
