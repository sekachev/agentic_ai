#!/usr/bin/env python3
"""
Скрипт для сбора данных с Instagram профиля profftech.ee
Использует instaloader для скачивания постов, фото и видео
"""

import os
import sys
from pathlib import Path
import instaloader
from datetime import datetime


# Настройки
PROFILE_NAME = "profftech.ee"
OUTPUT_DIR = Path("data/instagram_profftech")


def download_instagram_profile():
    """Скачивает данные Instagram профиля"""
    print("=" * 60)
    print(f"📸 Instagram парсер для профиля: {PROFILE_NAME}")
    print(f"📁 Данные будут сохранены в: {OUTPUT_DIR.absolute()}")
    print("=" * 60)
    
    # Создаем папку для вывода
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    # Инициализируем instaloader
    L = instaloader.Instaloader(
        dirname_pattern=str(OUTPUT_DIR / "{target}"),
        filename_pattern="{date_utc}_UTC_{shortcode}",
        download_pictures=True,
        download_videos=True,
        download_video_thumbnails=True,
        download_geotags=True,
        download_comments=True,
        save_metadata=True,
        compress_json=False,
    )
    
    try:
        print(f"\n🔄 Загрузка профиля {PROFILE_NAME}...")
        
        # Получаем профиль
        profile = instaloader.Profile.from_username(L.context, PROFILE_NAME)
        
        # Информация о профиле
        print(f"\n📊 Информация о профиле:")
        print(f"   Имя: {profile.full_name}")
        print(f"   Био: {profile.biography}")
        print(f"   Подписчиков: {profile.followers}")
        print(f"   Подписок: {profile.followees}")
        print(f"   Постов: {profile.mediacount}")
        print(f"   Подтвержден: {profile.is_verified}")
        print(f"   Бизнес-аккаунт: {profile.is_business_account}")
        
        # Сохраняем информацию о профиле в текстовый файл
        info_file = OUTPUT_DIR / "profile_info.txt"
        with open(info_file, 'w', encoding='utf-8') as f:
            f.write(f"Instagram Profile: {PROFILE_NAME}\n")
            f.write(f"Downloaded at: {datetime.now().isoformat()}\n")
            f.write("=" * 60 + "\n\n")
            f.write(f"Full Name: {profile.full_name}\n")
            f.write(f"Biography: {profile.biography}\n")
            f.write(f"Followers: {profile.followers}\n")
            f.write(f"Following: {profile.followees}\n")
            f.write(f"Posts: {profile.mediacount}\n")
            f.write(f"Verified: {profile.is_verified}\n")
            f.write(f"Business Account: {profile.is_business_account}\n")
            f.write(f"External URL: {profile.external_url or 'N/A'}\n\n")
        
        print(f"\n💾 Информация о профиле сохранена: {info_file}")
        
        # Скачиваем посты
        print(f"\n🔄 Начинаем скачивание {profile.mediacount} постов...")
        
        posts_downloaded = 0
        for post in profile.get_posts():
            try:
                L.download_post(post, PROFILE_NAME)
                posts_downloaded += 1
                
                if posts_downloaded % 10 == 0:
                    print(f"   ✓ Скачано {posts_downloaded}/{profile.mediacount} постов...")
                
            except Exception as e:
                print(f"   ✗ Ошибка при скачивании поста {post.shortcode}: {e}")
                continue
        
        print(f"\n" + "=" * 60)
        print(f"✅ Готово! Скачано постов: {posts_downloaded}")
        print(f"📁 Данные сохранены в: {OUTPUT_DIR.absolute()}")
        print("=" * 60)
        
        return True
        
    except instaloader.exceptions.ProfileNotExistsException:
        print(f"✗ Профиль {PROFILE_NAME} не существует!")
        return False
    except instaloader.exceptions.ConnectionException as e:
        print(f"✗ Ошибка подключения: {e}")
        return False
    except Exception as e:
        print(f"✗ Ошибка: {e}")
        return False


def main():
    """Точка входа"""
    # Проверяем установку instaloader
    try:
        import instaloader
        print(f"✓ instaloader установлен")
    except ImportError:
        print("✗ instaloader не установлен!")
        print("Установите командой: pip install instaloader")
        sys.exit(1)
    
    # Запускаем загрузку
    success = download_instagram_profile()
    
    if not success:
        sys.exit(1)


if __name__ == "__main__":
    main()
