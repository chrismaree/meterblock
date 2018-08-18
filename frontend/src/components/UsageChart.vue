<template>
  <div class="usagechart">
    <p>Enter the Meter Public key<p/>
    <input v-model="meterKey" name="key" class="input">
    <br>    
    {{meterData}}
    <br>
    <br>
    {{meterDataFeed}}
    <br>
    <el-button type="submit" @click="findMeter" class="button is-primary is-fullwidth subtitle">Find Meter</el-button>
    <br>
    
    <chart :type="'bar'" :data="meterDataFeed" :options="options"></chart>

  </div>
</template>

 <script>
import Chart from "vue-bulma-chartjs";

export default {
  name: "UsageChart",
  components: {
    Chart
  },

  data() {
    return {
      options: {
        segmentShowStroke: false,
        scales: {
          yAxes: [
            {
              display: true,
              ticks: {
                suggestedMin: 0 // minimum will be 0, unless there is a lower value.
              }
            }
          ]
        }
      },
      meterData: {
        lables: [],
        values: [],
        tokens: []
      },
      meterKey: '',
      labels: [0,1,2,3,4],
          
      data: [0,1,2,3,4],
    };
  },
  methods: {
    findMeter() {
      console.log(this.$data.meterData);
      let lables = [];
      let values = [];
      let tokens = [];
      this.$gun
        .get(this.$data.meterKey)
        .map()
        .on(function(value, time) {
          console.log({ time: time, value: value });
          lables.push(time);
          values.push(value.power);
          tokens.push(value.tokens);
          // this.$data.meterData.push({ time: time, value: value });
        });
      this.$data.meterData.lables.push(lables);
      this.$data.meterData.values.push(values);
      this.$data.meterData.tokens.push(tokens);
      console.log(this.$data.meterData);    
    }
  },
  computed: {
    meterDataFeed() {
      // return {
      //   labels: this.$data.data.lables,
      //   datasets: this.$data.data.datasets
      // };

      // return {
      // 	labels: this.$data.meterData.lables[0],
      // 	datasets: [{
      // 		label: 'Live Data',
      // 		data: this.$data.meterData.values[0],
      // 		backgroundColor: 'rgba(31, 200, 219, 1)'
      // 	}]
      // }
      
      
  
      
        if (this.$data.meterData.values.length[0]==undefined){
        return {
          labels: [0,1,2,3,4],
          datasets: [
            {
              data: [0,1,2,3,4],
              backgroundColor: "#1fc8db"
            }
          ]
        };
      }


        return {
          labels: this.$data.meterData.lables[0],
          datasets: [
            {
              data: this.$data.meterData.values[0],
              backgroundColor: Array.apply(
                null,
                Array(this.$data.meterData.values[0].length)
              ).map(String.prototype.valueOf, "#1fc8db")
            }
          ]
        };
      
        
    }
  }
};
</script>