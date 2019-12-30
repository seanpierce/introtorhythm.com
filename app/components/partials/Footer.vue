<template>
    <div id="footer">
        <ul>
            <li>
                <a href="/archive" target="_blank">Full Archive</a>
            </li>
            <li>
                <a href="https://introtorhythm.com/stream" target="_blank">stream.mp3</a>
            </li>
            <li>
                <a href="https://introtorhythm.com/stream/m3u" target="_blank">stream.m3u</a>
            </li>
            <li>
                ITR &copy; {{ year }}
            </li>
        </ul>
    </div>
</template>

<script>
export default {
    computed: {
        year() {
            return new Date().getFullYear();
        }
    }
}
</script>