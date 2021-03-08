USER_TYPE_CHOICES = (
    ('admin', 'Администратор'),
    ('manager', 'Менеджер'),
    ('user', 'Пользователь'),
)

NOTIFICATION_TYPE_CHOICES = (
    ('invoice', 'Запрос'),
)

NOTIFICATION_STATUS_CHOICES = (
    ('none', 'Не прочитано'),
    ('agree', 'Подтверждено'),
    ('disagree', 'Отказано'),
)

STATUS_TYPE_CHOICES = (
    ('free', 'свободный'),
    ('busy', 'занятый'),
)
STACK_CHOICES = (
    ('0', 'frontend'),
    ('1', 'backend'),
    ('2', 'fullstack'),
    ('3', 'ui ux design'),
)
