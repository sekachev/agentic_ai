import React from 'react';
import {
    Img,
    interpolate,
    spring,
    useCurrentFrame,
    useVideoConfig,
    staticFile
} from 'remotion';

interface Props {
    delay: number;
    y: number;
    x: number;
    hasTomato: boolean;
    hasOnion: boolean;
    scale?: number;
    opacity?: number;
}

export const Bowl: React.FC<Props> = ({ delay, y, x, hasTomato, hasOnion, scale: customScale = 1, opacity: customOpacity = 1 }) => {
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

    const s = interpolate(progress, [0, 1], [0.8 * customScale, 1 * customScale]);
    const entryOpacity = interpolate(progress, [0, 1], [0, 1]);
    const finalOpacity = entryOpacity * customOpacity;

    return (
        <div
            style={{
                position: 'absolute',
                left: x,
                top: y,
                transform: `translate(-50%, -50%) scale(${s})`,
                opacity: finalOpacity,
                width: 500,
                height: 500,
                display: 'flex',
                justifyContent: 'center',
                alignItems: 'center',
            }}
        >
            {/* Bowl Image */}
            <Img
                src={staticFile('assets_no_bg/bowl.png')}
                style={{
                    width: '100%',
                    height: '100%',
                    objectFit: 'contain',
                    filter: 'drop-shadow(0 20px 40px rgba(0,0,0,0.3))',
                }}
            />

            {/* Chopped Tomato inside bowl */}
            {hasTomato && (
                <div style={{
                    position: 'absolute',
                    top: '45%',
                    left: '50%',
                    width: '60%',
                    transform: 'translate(-50%, -50%) rotate(-5deg)',
                }}>
                    <Img
                        src={staticFile('assets_no_bg/chopped_tomato.png')}
                        style={{
                            width: '120%',
                            marginLeft: '-10%',
                            filter: 'drop-shadow(0 5px 10px rgba(0,0,0,0.2))'
                        }}
                    />
                </div>
            )}

            {/* Chopped Onion inside bowl */}
            {hasOnion && (
                <div style={{
                    position: 'absolute',
                    top: '40%',
                    left: '55%',
                    width: '50%',
                    transform: 'translate(-50%, -50%) rotate(10deg)',
                }}>
                    <Img
                        src={staticFile('assets_no_bg/chopped_onion.png')}
                        style={{
                            width: '120%',
                            marginLeft: '-10%',
                            filter: 'drop-shadow(0 5px 10px rgba(0,0,0,0.2))'
                        }}
                    />
                </div>
            )}
        </div>
    );
};
