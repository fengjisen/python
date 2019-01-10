# 一台服务器如何在网络中找到另一台服务器
# osi五层模型
    # 应用层
    # 传输层      tcp协议和udp协议
    # 网络层      ip协议(ipv4 ipv6)    路由器
    # 数据链路层  arp协议(利用ip找mac) 交换机
    # 物理层
# tcp协议  可靠地 面向连接的 字节流传输
# udp协议  不可靠的 无连接的 高效的传输
# TCP协议中 三次握手和四次挥手
# 粘包 针对 tcp协议
    # 拆包机制 nagel算法(合包) 缓存机制
    # 面向流的传输 - 数据与数据之间没有边界
    # 粘包机制可能发生在发送端和接收端
# udp协议不会粘包
    # 面向数据包的传输方式
    # 不可靠
# 对于空消息:
    # tcp协议不能发空消息
    # udp协议可以

