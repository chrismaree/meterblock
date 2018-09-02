// LineChart.js
import {
    Bar,
    mixins
} from 'vue-chartjs'

export default {
    extends: Bar,
    mixins: [mixins.reactiveProp],
    props: ['chartData', 'options'],
    mounted() {
        this.renderChart(this.data, this.options)
    }
}