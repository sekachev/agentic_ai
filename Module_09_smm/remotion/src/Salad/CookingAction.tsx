import React from 'react';
import {
    interpolate,
    spring,
    useCurrentFrame,
    useVideoConfig,
} from 'remotion';

interface Props {
    delay: number;
    text: string;
    x: number;
    y: number;
}

export const CookingAction: React.FC<Props> = ({ delay, text, x, y }) => {
    const frame = useCurrentFrame();
    const { fps } = useVideoConfig();

    const progress = spring({
        frame: frame - delay,
        fps,
        config: {
            damping: 12,
        },
    });

    if (frame < delay) {
        return null;
    }

    const opacity = interpolate(progress, [0, 1], [0, 1]);
    const scale = interpolate(progress, [0, 1], [0.5, 1]);

    return (
        <div
            style={{
                position: 'absolute',
                left: x,
                top: y,
                transform: `translate(-50%, -50%) scale(${scale})`,
                opacity,
                display: 'flex',
                flexDirection: 'row',
                alignItems: 'center',
                zIndex: 10,
            }}
        >
            <div
                style={{
                    fontSize: '60px',
                    color: '#ff7675',
                    lineHeight: 1,
                    marginRight: '15px',
                }}
            >
                →
            </div>
            <div
                style={{
                    background: '#ff7675',
                    color: 'white',
                    padding: '8px 20px',
                    borderRadius: '15px',
                    fontSize: '24px',
                    fontWeight: '900',
                    textTransform: 'uppercase',
                    boxShadow: '0 10px 20px rgba(255, 118, 117, 0.3)',
                    whiteSpace: 'nowrap'
                }}
            >
                {text}
            </div>
        </div>
    );
};
