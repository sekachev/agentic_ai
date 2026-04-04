import asyncio
import argparse
import edge_tts

async def generate_voice(text: str, voice: str, output: str) -> None:
    """
    Генерирует аудио из текста с использованием edge-tts.
    """
    try:
        communicate = edge_tts.Communicate(text, voice)
        await communicate.save(output)
        print(f"✅ Аудио успешно сохранено: {output}")
    except Exception as e:
        print(f"❌ Ошибка при генерации: {e}")

async def main() -> None:
    parser = argparse.ArgumentParser(description="Edge TTS Generator")
    parser.add_argument("-t", "--text", default="Вот что я хочу тебе сказать, генерация голоса - это просто! Как раз-два-три", help="Текст для озвучки")
    parser.add_argument("-v", "--voice", default="ru-RU-DmitryNeural", help="Голос (например, ru-RU-DmitryNeural)")
    parser.add_argument("-o", "--output", default="test.mp3", help="Имя выходного файла")
    
    args = parser.parse_args()

    await generate_voice(args.text, args.voice, args.output)

if __name__ == "__main__":
    asyncio.run(main())
