# Content Management

Здесь хранится весь создаваемый контент.

## Структура

- `raw_events/` — Входящие инфоповоды и идеи.
- `weeks/` — Основное хранилище постов:
    - `YYYY-WW/` (например, `2024-W06/`)
        - `plan.md` — Контент-план на эту неделю.
        - `YYYY-MM-DD/` (например, `2024-02-10/`)
            - `ig_post.md` — Пост для Instagram.
            - `fb_post.md` — Пост для Facebook.
            - `image.jpg` — Картинка для этого поста.

## Работа со статусами

В каждом `.md` файле поста должен быть блок YAML Frontmatter:

```yaml
---
status: draft | approved | scheduled | published
platform: Instagram
publish_date: 2024-02-10
event_ref: ../../../raw_events/event-id.md
---
```

Медиа-файлы ищутся скриптами в той же директории, где лежит `.md` файл.
