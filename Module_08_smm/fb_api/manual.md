
### Шаг 0: Подготовка (Бюрократия)
Чтобы API работало, твоя цепочка должна выглядеть так:
1.  **Аккаунт Instagram** должен быть переведен в статус **Business** или **Creator** (в настройках приложения).
2.  **Facebook Page:** У тебя должна быть публичная страница Facebook (не личный профиль).
3.  **Связка:** В настройках Facebook Page нужно привязать твой Instagram-аккаунт.

---

### Шаг 1: Meta for Developers
1.  Иди на [developers.facebook.com](https://developers.facebook.com/) и создай аккаунт разработчика.
2.  **Создай приложение:** Тип приложения выбирай **"Other"**, затем на следующем шаге — **"Business"**.
3.  В панели управления приложением добавь продукт **"Instagram Graph API"**.

---

### Шаг 2: Получение токенов (Самое важное)
Тебе понадобятся три вещи:
*   `Access Token` (ключ доступа).
*   `Instagram Business Account ID` (ID твоего аккаунта, а не имя пользователя).

**Как быстро получить всё для теста:**
1.  Зайди в **Graph API Explorer**.
2.  Выбери своё приложение.
3.  В разрешениях (Permissions) добавь:
    *   `instagram_basic`
    *   `instagram_content_publish`
    *   `instagram_manage_comments`
    *   `pages_show_list`
    *   `pages_read_engagement`
4.  Нажми "Generate Access Token" и разреши доступ к своей странице и инстаграму.
5.  Сделай запрос `GET /me/accounts`, чтобы найти `access_token` страницы и её ID.
6.  Сделай запрос `GET /{page-id}?fields=instagram_business_account`, чтобы получить **IG User ID**.

