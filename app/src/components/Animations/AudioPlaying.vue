<template>
    <div class="audio-playing">
        <div class="audio-playing__block first-block"></div>
        <div class="audio-playing__block second-block"></div>
        <div class="audio-playing__block third-block"></div>
    </div>
</template>

<style scoped>
.audio-playing {
    display: table-cell;
    vertical-align: middle;
    padding: 4px 14px 4px 0;
}

.audio-playing__block {
    display: inline-block;
    width: 4px;
    height: 20px;
    background-color: red;
    margin-right: 2px;
}

@keyframes first-block {
    0% { transform: scaleY(1); }
    25% { transform: scaleY(0.6); }
    50% { transform: scaleY(0.4); }
    100% { transform: scaleY(1); }
}

.audio-playing__block.first-block {
    animation-name: first-block;
    animation-duration: 1.5s;
    animation-iteration-count: infinite;
    animation-timing-function: linear;
}

@keyframes second-block {
    0% { transform: scaleY(1); }
    25% { transform: scaleY(0.3); }
    50% { transform: scaleY(0.5); }
    100% { transform: scaleY(1); }
}

.audio-playing__block.second-block {
    animation-name: second-block;
    animation-duration: 1.75s;
    animation-iteration-count: infinite;
    animation-timing-function: linear;
}

@keyframes third-block {
    0% { transform: scaleY(1); }
    25% { transform: scaleY(0.9); }
    50% { transform: scaleY(0.2); }
    100% { transform: scaleY(1); }
}

.audio-playing__block.third-block {
    animation-name: third-block;
    animation-duration: 1.25s;
    animation-iteration-count: infinite;
    animation-timing-function: linear;
}
</style>