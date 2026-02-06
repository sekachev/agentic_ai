import React from 'react';
import { useCurrentFrame, useVideoConfig } from 'remotion';

export const SaladBackground: React.FC = () => {
    const frame = useCurrentFrame();
    const { width, height } = useVideoConfig();

    // Create a subtle moving gradient
    return (
        <div
            style={{
                position: 'absolute',
                width,
                height,
                background: `radial-gradient(circle at ${50 + Math.sin(frame / 60) * 10}% ${50 + Math.cos(frame / 60) * 10
                    }%, #fdfcfb 0%, #e2d1c3 100%)`,
                display: 'flex',
                justifyContent: 'center',
                alignItems: 'center',
                overflow: 'hidden',
            }}
        >
            {/* Decorative elements */}
            {[...Array(5)].map((_, i) => (
                <div
                    key={i}
                    style={{
                        position: 'absolute',
                        width: 400,
                        height: 400,
                        borderRadius: '50%',
                        background: 'rgba(255, 255, 255, 0.3)',
                        filter: 'blur(80px)',
                        left: `${(i * 30) % 100}%`,
                        top: `${(i * 40) % 100}%`,
                        transform: `translate(-50%, -50%) scale(${1 + Math.sin((frame + i * 20) / 40) * 0.2})`,
                    }}
                />
            ))}
        </div>
    );
};
