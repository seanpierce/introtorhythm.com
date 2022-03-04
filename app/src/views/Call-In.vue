<script>
export default {
    mounted() {
        let link = document.createElement('a')
        link.href = 'tel:9713949073'
        link.click()
        this.$router.push('/')
    }
}
</script>