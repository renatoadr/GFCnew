from flask import flash, get_flashed_messages


class flash_message:
    @staticmethod
    def error(message: str):
        flash(message, category='error')

    @staticmethod
    def warning(message: str):
        flash(message, category='warning')

    @staticmethod
    def info(message: str):
        flash(message, category='info')

    @staticmethod
    def has_error():
        return flash_message.has('error')

    @staticmethod
    def has_warning():
        return flash_message.has('warning')

    @staticmethod
    def has_info():
        return flash_message.has('info')

    @staticmethod
    def has(category: str):
        msgs = get_flashed_messages(category_filter=[category])
        return len(msgs) > 0
