config = {
    "interfaces": {
        "google.cloud.memcache.v1beta2.CloudMemcache": {
            "retry_codes": {"no_retry_codes": [], "no_retry_1_codes": []},
            "retry_params": {
                "no_retry_params": {
                    "initial_retry_delay_millis": 0,
                    "retry_delay_multiplier": 0.0,
                    "max_retry_delay_millis": 0,
                    "initial_rpc_timeout_millis": 0,
                    "rpc_timeout_multiplier": 1.0,
                    "max_rpc_timeout_millis": 0,
                    "total_timeout_millis": 0,
                },
                "no_retry_1_params": {
                    "initial_retry_delay_millis": 0,
                    "retry_delay_multiplier": 0.0,
                    "max_retry_delay_millis": 0,
                    "initial_rpc_timeout_millis": 1200000,
                    "rpc_timeout_multiplier": 1.0,
                    "max_rpc_timeout_millis": 1200000,
                    "total_timeout_millis": 1200000,
                },
            },
            "methods": {
                "ListInstances": {
                    "timeout_millis": 60000,
                    "retry_codes_name": "no_retry_1_codes",
                    "retry_params_name": "no_retry_1_params",
                },
                "GetInstance": {
                    "timeout_millis": 60000,
                    "retry_codes_name": "no_retry_1_codes",
                    "retry_params_name": "no_retry_1_params",
                },
                "CreateInstance": {
                    "timeout_millis": 1200000,
                    "retry_codes_name": "no_retry_1_codes",
                    "retry_params_name": "no_retry_1_params",
                },
                "UpdateInstance": {
                    "timeout_millis": 1200000,
                    "retry_codes_name": "no_retry_1_codes",
                    "retry_params_name": "no_retry_1_params",
                },
                "UpdateParameters": {
                    "timeout_millis": 1200000,
                    "retry_codes_name": "no_retry_1_codes",
                    "retry_params_name": "no_retry_1_params",
                },
                "DeleteInstance": {
                    "timeout_millis": 1200000,
                    "retry_codes_name": "no_retry_1_codes",
                    "retry_params_name": "no_retry_1_params",
                },
                "ApplyParameters": {
                    "timeout_millis": 1200000,
                    "retry_codes_name": "no_retry_1_codes",
                    "retry_params_name": "no_retry_1_params",
                },
            },
        }
    }
}
