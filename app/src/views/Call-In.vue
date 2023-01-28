<script>
const apiClient = require('@/utilities/apiClient')

export default {
    methods: {
        getCallInNumber() {
            apiClient.get('content/call-in')
                .then(response => {
                    let link = document.createElement('a')
                    link.href = `tel:${response.phone_number}`
                    link.click()
                    this.$router.push('/')
                })
        }
    },

    mounted() {
        this.getCallInNumber()
    }
}
</script>