#!/usr/bin/env python3
"""
Скрипт для сбора данных с сайта tetkool.ee
Использует crawl4ai для парсинга в markdown с сохранением структуры папок
"""

import os
import asyncio
import json
from pathlib import Path
from urllib.parse import urlparse, urljoin
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
from crawl4ai.content_filter_strategy import PruningContentFilter
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator


# Базовый URL сайта
BASE_URL = "https://tetkool.ee"

# Папка для сохранения данных
OUTPUT_DIR = Path("data/tetkool_site")

# URLs для парсинга (начальные точки)
START_URLS = [
    "https://tetkool.ee/",
    "https://tetkool.ee/training/",           # Курсы (RU)
    "https://tetkool.ee/about-us/",           # О нас (RU)
    "https://tetkool.ee/about-us/teachers/",  # Преподаватели (RU)
    "https://tetkool.ee/contacts-us/",        # Контакты (RU)
    "https://tetkool.ee/et/training/",        # Курсы (ET)
    "https://tetkool.ee/et/about-us/",        # О нас (ET)
    "https://tetkool.ee/et/about-us/teachers/",  # Преподаватели (ET)
    "https://tetkool.ee/en/",                 # Главная (EN)
]


def get_local_path(url: str) -> Path:
    """Преобразует URL в локальный путь для сохранения"""
    parsed = urlparse(url)
    path = parsed.path.strip('/')
    
    # Если путь пустой, это главная страница
    if not path:
        return OUTPUT_DIR / "index.md"
    
    # Создаем путь из URL
    local_path = OUTPUT_DIR / path
    
    # Если URL заканчивается на /, добавляем index.md
    if url.endswith('/'):
        local_path = local_path / "index.md"
    else:
        # Иначе добавляем .md расширение
        local_path = local_path.with_suffix('.md')
    
    return local_path


def save_markdown(url: str, content: str, metadata: dict = None):
    """Сохраняет markdown контент в файл, сохраняя структуру папок"""
    local_path = get_local_path(url)
    
    # Создаем директории если нужно
    local_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Добавляем метаданные в начало файла
    header = f"""---
url: {url}
"""
    if metadata:
        for key, value in metadata.items():
            header += f"{key}: {value}\n"
    header += "---\n\n"
    
    # Сохраняем файл
    with open(local_path, 'w', encoding='utf-8') as f:
        f.write(header + content)
    
    print(f"  ✓ Сохранено: {local_path}")
    return local_path


async def crawl_single_page(crawler: AsyncWebCrawler, url: str):
    """Парсит одну страницу и сохраняет в markdown"""
    try:
        print(f"\n🔄 Парсинг: {url}")
        
        result = await crawler.arun(url=url)
        
        if result.success:
            # Получаем markdown контент (новый API crawl4ai 0.8+)
            markdown_content = result.markdown.raw_markdown
            
            # Метаданные
            metadata = {
                'title': result.metadata.get('title', ''),
                'description': result.metadata.get('description', ''),
                'crawled_at': str(asyncio.get_event_loop().time()),
            }
            
            # Сохраняем
            save_path = save_markdown(url, markdown_content, metadata)
            
            # Сохраняем ссылки для дальнейшего парсинга
            internal_links = result.links.get('internal', [])
            # Извлекаем URL из словарей ссылок
            links = [link.get('href', link) if isinstance(link, dict) else link for link in internal_links]
            
            return {
                'success': True,
                'url': url,
                'path': str(save_path),
                'links': links,
                'metadata': metadata
            }
        else:
            print(f"  ✗ Ошибка при парсинге {url}: {result.error_message}")
            return {'success': False, 'url': url, 'error': result.error_message}
            
    except Exception as e:
        print(f"  ✗ Исключение при парсинге {url}: {str(e)}")
        return {'success': False, 'url': url, 'error': str(e)}


async def crawl_site():
    """Основная функция для сбора данных с сайта"""
    print("=" * 60)
    print(f"🕷️  Начинаем сбор данных с {BASE_URL}")
    print(f"📁 Данные будут сохранены в: {OUTPUT_DIR.absolute()}")
    print("=" * 60)
    
    # Создаем папку для вывода
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    # Настройки браузера
    browser_config = BrowserConfig(
        headless=True,
        verbose=False,
    )
    
    # Настройки краулера
    crawl_config = CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS,
        markdown_generator=DefaultMarkdownGenerator(
            content_filter=PruningContentFilter(threshold=0.5),
            options={
                'ignore_links': False,
                'ignore_images': False,
            }
        ),
    )
    
    results = []
    all_links = set()
    
    async with AsyncWebCrawler(config=browser_config) as crawler:
        # Парсим начальные URL
        for url in START_URLS:
            result = await crawl_single_page(crawler, url)
            results.append(result)
            
            if result['success']:
                all_links.update(result.get('links', []))
        
        # Сохраняем найденные ссылки для дальнейшего использования
        links_file = OUTPUT_DIR / "_discovered_links.json"
        with open(links_file, 'w', encoding='utf-8') as f:
            json.dump({
                'base_url': BASE_URL,
                'discovered_links': list(all_links),
                'crawled_pages': [r['url'] for r in results if r['success']]
            }, f, ensure_ascii=False, indent=2)
        
        print(f"\n📋 Найдено {len(all_links)} ссылок, сохранено в {links_file}")
    
    # Статистика
    successful = len([r for r in results if r['success']])
    print(f"\n" + "=" * 60)
    print(f"✅ Готово! Успешно спарсено: {successful}/{len(START_URLS)} страниц")
    print(f"📁 Данные сохранены в: {OUTPUT_DIR.absolute()}")
    print("=" * 60)
    
    return results


def main():
    """Точка входа"""
    # Проверяем установку crawl4ai
    try:
        import crawl4ai
        print(f"✓ crawl4ai установлен (версия: {crawl4ai.__version__})")
    except ImportError:
        print("✗ crawl4ai не установлен!")
        print("Установите командой: pip install crawl4ai")
        return
    
    # Запускаем асинхронный сбор данных
    asyncio.run(crawl_site())


if __name__ == "__main__":
    main()
