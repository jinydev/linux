# 가상머신 네트워크

![스크린샷 2023-04-24 오전 9.14.21.png](/img/표.png)

## Host-only

Host-only 방식부터 알아보겠다.

> 이 방식은 가상머신 내에 존재하는 컴퓨터끼리만 통신이 가능한 것을 말한다.
> 
- 외부와 단절된 내부 네트워크이다.
- 가상머신들 사이에서만 통신이 가능하다.
- 호스트와의 통신은 가능하다.

![https://velog.velcdn.com/images/duck-ach/post/c44c1ea5-348c-42e6-8119-561e824de694/image.png](https://velog.velcdn.com/images/duck-ach/post/c44c1ea5-348c-42e6-8119-561e824de694/image.png)

## 내부 네트워크

Host-only와 유사하지만 내부 가상머신간의 통시만 가능하다.

> 이 방식은 가상머신 내에 존재하는 컴퓨터끼리만 통신이 가능한 것을 말한다. 호스트와의 통신도 불가능하다.
> 
- 외부와 단절된 내부 네트워크이다.
- 가상머신들 사이에서만 통신이 가능하다.
- 호스트와의 통신도 불가능 하다.

## NAT(Network Address Translation)

네트워크 주소 변환이라고도 하는 NAT은 Host PC로부터 IP를 할당받기 때문에 가상머신이 자체적으로 DHCP Server를 통해 내부 네트워크 대역을 할당 및 통신을 하며, 호스트 PC를 통해 외부 네트워크와 통신이 가능하다.

> DHCP Server :Dynamic Host Configuration Protocol의 약자로 동적 호스트 설정 통신 규약이다.IP ADDRESS, NETMASK, GATEWAY 등의 설정을 자동으로 해준다.
> 
- Host PC로부터 ip를 할당받는다.
- Host PC는 공유기로부터 ip를 할당받는다.
- Host PC를 통해 외부 네트워크와 통신한다.

![https://velog.velcdn.com/images/duck-ach/post/27ad9342-49cd-444b-b05c-fe8edc296afd/image.png](https://velog.velcdn.com/images/duck-ach/post/27ad9342-49cd-444b-b05c-fe8edc296afd/image.png)

## Bridged

Bridged 방식은 공유기로부터 IP를 할당받아 Host PC와 동일한 네트워크 대역의 IP를 가지게 된다.따라서, 외부와의 통신이 가능하다.

Bridged Networking은 외부로 노출이 되기 때문에 외부에서 가상 머신으로 직접 접근하는 것이 가능하며, 사설망에서 컴퓨터끼리 공유 폴더 등으로 접근이 가능하듯 다른 컴퓨터와 동등하게 사용이 가능하다.

- 공유기로부터 ip를 할당받는다.
- Host PC와 동일한 네트워크 대역의 ip를 갖는다.
- 공유기를 통해 외부 네트워크와 통신한다.

![https://velog.velcdn.com/images/duck-ach/post/a71a205a-3e2b-4075-a792-e68c17973f34/image.png](https://velog.velcdn.com/images/duck-ach/post/a71a205a-3e2b-4075-a792-e68c17973f34/image.png)

### NAT과 Bridged의 차이점

가상머신의 IP 할당을 주는 곳 차이

NAT는 Host PC, Bridge는 공유기