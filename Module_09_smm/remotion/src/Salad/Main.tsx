import React from 'react';
import { AbsoluteFill, staticFile, useVideoConfig, interpolate, useCurrentFrame, spring } from 'remotion';
import { Ingredient } from './Ingredient';
import { SaladBackground } from './Background';
import { CookingAction } from './CookingAction';
import { Bowl } from './Bowl';

export const SaladMain: React.FC = () => {
    const frame = useCurrentFrame();
    const { width, height, fps } = useVideoConfig();

    const topY = height * 0.3;
    const bottomY = height * 0.7;

    // Animation to clear the screen at the end
    const exitProgress = spring({
        frame: frame - 250,
        fps,
        config: { damping: 20 }
    });

    const contentOpacity = interpolate(exitProgress, [0, 1], [1, 0]);

    // Final bowl transition
    const finalBowlAppear = spring({
        frame: frame - 255,
        fps,
        config: { damping: 12 }
    });

    const finalBowlPos = {
        x: interpolate(finalBowlAppear, [0, 1], [width * 0.9, width / 2]),
        y: interpolate(finalBowlAppear, [0, 1], [bottomY, height / 2]),
        scale: interpolate(finalBowlAppear, [0, 1], [0.6, 1.5]),
    };

    return (
        <AbsoluteFill>
            <SaladBackground />

            <div style={{ opacity: contentOpacity }}>
                {/* --- TOP ROW: TOMATOES --- */}
                <div style={{ position: 'absolute', left: 80, top: topY - 180, fontFamily: 'system-ui', fontSize: 48, fontWeight: 900, color: '#e17055', textTransform: 'uppercase' }}>
                    1. Помидоры
                </div>

                <Ingredient
                    src={staticFile('assets_no_bg/tomato.png')}
                    label="Целый"
                    weight="250г"
                    delay={10}
                    x={width * 0.2}
                    y={topY}
                />

                <CookingAction delay={35} text="Режем" x={width * 0.4} y={topY} />

                <Ingredient
                    src={staticFile('assets_no_bg/chopped_tomato.png')}
                    label="Нарезанный"
                    weight="Кубики"
                    delay={55}
                    x={width * 0.6}
                    y={topY}
                />

                <CookingAction delay={80} text="В миску" x={width * 0.8} y={topY} />
                <Bowl delay={100} y={topY} x={width * 0.95} hasTomato={true} hasOnion={false} scale={0.5} />

                {/* Horizontal Divider */}
                <div style={{
                    position: 'absolute',
                    top: '50%',
                    left: '5%',
                    width: '90%',
                    height: '2px',
                    background: 'rgba(0,0,0,0.1)',
                }} />

                {/* --- BOTTOM ROW: ONIONS --- */}
                <div style={{ position: 'absolute', left: 80, top: bottomY - 180, fontFamily: 'system-ui', fontSize: 48, fontWeight: 900, color: '#00b894', textTransform: 'uppercase' }}>
                    2. Зеленый лук
                </div>

                <Ingredient
                    src={staticFile('assets_no_bg/onion.png')}
                    label="Свежий"
                    weight="50г"
                    delay={130}
                    x={width * 0.2}
                    y={bottomY}
                />

                <CookingAction delay={155} text="Шинкуем" x={width * 0.4} y={bottomY} />

                <Ingredient
                    src={staticFile('assets_no_bg/chopped_onion.png')}
                    label="Кольца"
                    weight="Тонко"
                    delay={175}
                    x={width * 0.6}
                    y={bottomY}
                />

                <CookingAction delay={200} text="В миску" x={width * 0.8} y={bottomY} />
            </div>

            {/* THE FINAL BOWL (Transitions to center at the end) */}
            <Bowl
                delay={220}
                y={frame > 255 ? finalBowlPos.y : bottomY}
                x={frame > 255 ? finalBowlPos.x : width * 0.95}
                hasTomato={true}
                hasOnion={true}
                scale={frame > 255 ? finalBowlPos.scale : 0.5}
            />
        </AbsoluteFill>
    );
};
