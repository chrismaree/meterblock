module.exports = {
    // See <http://truffleframework.com/docs/advanced/configuration>
    // for more about customizing your Truffle configuration!
    networks: {
        development: {
            host: "127.0.0.1",
            port: 8545,
            network_id: "*" // Match any network id
        },
        
        lan: {
            host: "10.0.0.206",
            port: 8545,
            network_id: "*"
        },

        dockerganache: {
            host: "142.93.131.22",
            port: 8545,
            network_id: "*"
        }
    }
};