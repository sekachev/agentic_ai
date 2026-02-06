"use client"

import type React from "react"
import { useCurrentFrame, useVideoConfig, AbsoluteFill, interpolate, random } from "remotion"

// Helper for deterministic scrambling based on frame
const getScrambledText = (phrase: string, frame: number, seed: string) => {
    const chars = '!<>-_\\/[]{}—=+*^?#'
    const phraseLength = phrase.length

    // Animation duration scaled by length
    const duration = Math.max(15, 35 - Math.floor(phraseLength / 3))
    // How many frames have passed in the current phrase cycle
    const localFrame = frame % 75

    let output = ''
    for (let i = 0; i < phraseLength; i++) {
        const charSeed = `${seed}-${phrase}-${i}`

        // Add a bias based on index 'i' so earlier letters start resolving sooner
        const indexBias = (i / phraseLength) * 20
        const randomBuffer = 75 - duration - 30 // Ensure it finishes before slide ends
        const start = Math.floor(indexBias + random(charSeed) * randomBuffer)
        const end = start + duration

        if (localFrame >= end) {
            output += phrase[i]
        } else if (localFrame >= start) {
            const charIndex = Math.floor(random(`${charSeed}-${localFrame}`) * chars.length)
            const char = chars[charIndex]
            output += `<span class="dud" style="color: #00ff00; opacity: 0.8;">${char}</span>`
        } else {
            output += '' // Hide or show previous? Let's show spaces
            output += ' '
        }
    }
    return output
}

const ScrambledTitle: React.FC = () => {
    const frame = useCurrentFrame()
    const { fps } = useVideoConfig()

    const phrases = [
        'Baltic Business Club',
        'Nikolay Sekachev',
        'presenting',
        'PROACTIVE',
        'AI AGENTS',
        'FOR YOUR BUSINESS',
        'Agents are built',
        'to fight routine',
        'in marketing, sales',
        'and admin tasks',
        'See you on Feb 12',
        'MOOS restaurant'
    ]

    // Each phrase stays for 2.5 seconds (75 frames at 30fps)
    const phraseDuration = 75
    const phraseIndex = Math.floor(frame / phraseDuration) % phrases.length
    const currentPhrase = phrases[phraseIndex]

    const scrambled = getScrambledText(currentPhrase, frame % phraseDuration, `phrase-${phraseIndex}`)

    return (
        <h1
            className="text-white text-9xl font-bold tracking-wider text-center"
            style={{ fontFamily: 'monospace' }}
            dangerouslySetInnerHTML={{ __html: scrambled }}
        />
    )
}

const RainingLetters: React.FC = () => {
    const frame = useCurrentFrame()
    const { width, height } = useVideoConfig()

    const charCount = 250
    const allChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;:,.<>?"

    const characters = Array.from({ length: charCount }).map((_, i) => {
        const seed = `char-${i}`
        const x = random(seed) * 100
        const initialY = random(`${seed}-y`) * 100
        const speed = 0.1 + random(`${seed}-speed`) * 0.4

        // Calculate current Y based on frame
        // y = (initialY + frame * speed) % 105 (to allow it to go slightly off screen)
        let y = (initialY + frame * speed) % 110
        if (y < 0) y += 110

        // Deterministic flicker
        // Change active status every 3 frames (~100ms at 30fps)
        const flickerSeed = Math.floor(frame / 3)
        const isActive = random(`${seed}-active-${flickerSeed}`) > 0.95

        // Random char changes periodically
        const charUpdateCycle = 20
        const charSeed = Math.floor((frame + initialY) / charUpdateCycle)
        const char = allChars[Math.floor(random(`${seed}-char-${charSeed}`) * allChars.length)]

        return { x, y, char, isActive }
    })

    return (
        <AbsoluteFill className="bg-black overflow-hidden">
            {/* Title */}
            <div className="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 z-20 w-full flex justify-center">
                <ScrambledTitle />
            </div>

            {/* Raining Characters */}
            {characters.map((char, index) => (
                <span
                    key={index}
                    className={`absolute text-xs transition-colors duration-100 ${char.isActive
                        ? "text-slate-200 font-bold"
                        : "text-slate-500 font-light"
                        }`}
                    style={{
                        left: `${char.x}%`,
                        top: `${char.y}%`,
                        transform: `translate(-50%, -50%) ${char.isActive ? 'scale(1.2)' : 'scale(1)'}`,
                        textShadow: char.isActive
                            ? '0 0 10px rgba(255,255,255,0.4), 0 0 20px rgba(255,255,255,0.2)'
                            : 'none',
                        opacity: char.isActive ? 0.8 : 0.4,
                        fontSize: char.isActive ? '2.4rem' : '1.8rem'
                    }}
                >
                    {char.char}
                </span>
            ))}
        </AbsoluteFill>
    )
}

export default RainingLetters
