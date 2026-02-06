import React from 'react';
import {
    Img,
    interpolate,
    spring,
    useCurrentFrame,
    useVideoConfig,
} from 'remotion';

interface Props {
    src: string;
    label: string;
    weight: string;
    delay: number;
    x: number;
    y: number;
}

export const Ingredient: React.FC<Props> = ({ src, label, weight, delay, x, y }) => {
    const frame = useCurrentFrame();
    const { fps } = useVideoConfig();

    const entryProgress = spring({
        frame: frame - delay,
        fps,
        config: {
            damping: 12,
        },
    });

    // Floating effect
    const floatOffset = Math.sin((frame - delay) / 20) * 15;
    const rotation = Math.sin((frame - delay) / 30) * 2;

    if (frame < delay) {
        return null;
    }

    const scale = interpolate(entryProgress, [0, 1], [0, 1]);
    const opacity = interpolate(entryProgress, [0, 1], [0, 1]);

    return (
        <div
            style={{
                position: 'absolute',
                left: x,
                top: y,
                transform: `translate(-50%, -50%) scale(${scale}) translateY(${floatOffset}px) rotate(${rotation}deg)`,
                opacity,
                display: 'flex',
                flexDirection: 'column',
                alignItems: 'center',
            }}
        >
            <div
                style={{
                    width: 400,
                    height: 400,
                    display: 'flex',
                    justifyContent: 'center',
                    alignItems: 'center',
                    overflow: 'hidden',
                }}
            >
                <Img
                    src={src}
                    style={{
                        width: '90%',
                        height: '90%',
                        objectFit: 'contain',
                    }}
                />
            </div>

            <div
                style={{
                    marginTop: -20,
                    textAlign: 'center',
                    fontFamily: 'system-ui, -apple-system, sans-serif',
                    background: 'rgba(255, 255, 255, 0.8)',
                    backdropFilter: 'blur(10px)',
                    padding: '12px 24px',
                    borderRadius: '30px',
                    boxShadow: '0 10px 30px rgba(0,0,0,0.1)',
                    border: '1px solid rgba(255, 255, 255, 0.5)',
                }}
            >
                <div
                    style={{
                        fontSize: '32px',
                        fontWeight: 'bold',
                        color: '#2d3436',
                        marginBottom: '4px',
                    }}
                >
                    {label}
                </div>
                <div
                    style={{
                        fontSize: '24px',
                        color: '#636e72',
                        fontWeight: '500',
                    }}
                >
                    {weight}
                </div>
            </div>
        </div>
    );
};
