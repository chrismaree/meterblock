<template>
  <div class="app">
<div class="center">
<el-menu class="center" mode="horizontal">  
<el-menu-item index="1">
    <router-link to="/about">About</router-link>
    </el-menu-item>

<el-menu-item index="2">
    <router-link to="/admin">Admin</router-link>
    </el-menu-item>
  
  <el-menu-item index="3">
    <router-link to="/metermanagement">Meter Management</router-link>
    </el-menu-item>
  
<el-menu-item index="4">
    <router-link to="/networkutilization">Network Utilization</router-link>
    </el-menu-item>
<el-menu-item index="5">
<el-button v-if="this.$store.state.isWalletUnlocked" type="success" @click="openEthereumModalSuccess" plain>Wallet Unlocked <i class="el-icon-circle-check"></i></el-button>
          <el-button v-if="!this.$store.state.isWalletUnlocked" type="warning" @click="openEthereumModalWarning" plain>Wallet Locked <i class="el-icon-circle-close"></i></el-button>
<el-button v-if="this.$store.state.gunDBNetworkState" type="success" @click="openGunDBModalSuccess" plain>GunDB Connected <i class="el-icon-circle-check"></i></el-button>
          <el-button v-if="!this.$store.state.gunDBNetworkState" type="warning" @click="openGunDBModalSuccess" plain>GunDB Connection Failed <i class="el-icon-circle-close"></i></el-button>
</el-menu-item>
</el-menu>
</div>
<br>
<el-card class="contentCard">
<router-view/>    
</el-card>
  </div>
</template>

<script>
export default {
  methods: {
    openEthereumModalSuccess() {
      let message =
        "<strong>Address: </strong>" +
        this.$store.state.defaultEthWallet +
        "<br><strong>Network: </strong>" +
        this.$store.state.netIdString +
        "<br><strong>Unlocked: </strong>" +
        this.$store.state.isWalletUnlocked;
      this.$alert(message, "Ethereum Blockchain Connected Correctly", {
        dangerouslyUseHTMLString: true,
        confirmButtonText: "OK",
        type: "Success",
        center: true
      });
    },

    openEthereumModalWarning() {
      let message =
        "<strong>Address: </strong>" +
        this.$store.state.defaultEthWallet +
        "<br><strong>Network: </strong>" +
        this.$store.state.netIdString +
        "<br><strong>Unlocked: </strong>" +
        this.$store.state.isWalletUnlocked;
      this.$alert(message, "Ethereum Blockchain NOT Connected Correctly", {
        dangerouslyUseHTMLString: true,
        confirmButtonText: "OK",
        type: "Success",
        center: true
      });
    },
    openGunDBModalSuccess() {
      let message =
        "<strong>GunDB Server: </strong>" +
        this.$store.state.gunDBNetworkAddress;
      this.$alert(message, "GunDB Connected Correctly", {
        dangerouslyUseHTMLString: true,
        confirmButtonText: "OK",
        type: "Success",
        center: true
      });
    }
  }
};
</script>


<style lang="scss">
.app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  // text-align: center;
  color: #2c3e50;
}
.nav {
  text-align: center;
  padding: 30px;
  a {
    font-weight: bold;
    color: #2c3e50;
    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
.center {
  text-align: center;
}
.contentCard{
      max-width: 1400px;
      margin: auto;
}
</style>
