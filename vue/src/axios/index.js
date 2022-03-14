// 1. 引入
import axios from "axios";

// 2. 创建实例
const instance = axios.create(config)
axios.defaults.baseURL = 'https://yinwei.icu:5000/v1/api';
// 3. 配置信息
let config = {
    // 每次请求的协议、IP地址。  设置该配置后，每次请求路径都可以使用相对路径，例如"/admin/login"
    baseURL: 'https://yinwei.icu:5000/v1/api',
    // 请求超时时间
    timeout: 10000,
    // 解决跨域问题
    // withCredentials: true,
    // headers: {"X-Requested-With": "XMLHttpRequest"},

}

// 4. 导出
export default instance