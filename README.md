# numer0n

いわゆる Hit&Blow (マスターマインドともいうらしい)

いまのところ3桁COM戦でつくっているけど
ゆくゆくは
PvP
だとか
アイテム使用
にも対応させていきたい

あとはCOMのレベルを上げていきたい
アルゴリズムの改善だとか
DBに過去データ格納して機械学習だとか？？？

body:本体

parts:関数とか機能面実装に関わる部分


【バージョン履歴】

v1.0:
プレイヤーが入力した数字をCOMがただあてるだけ

eatとbiteは判断してる

重複なしで1/720を当てるまでひたすらランダム

v1.1:
あてるまでに何回かかったか数えている

enterキーでexitできるようにした

continueかexitかを選べるようにした

20190826

v1.2:
同じ処理を関数にまとめた

judgeにまとめるかバラバラのほうがいいかは要検討

関数の返り値をリストにするか、それぞれの値にするかも要検討

ここからreturn_valueとreturn_listでブランチでわける


valueのほうがよさそうなのでvalueでつくっていく


(value)v1.3:

judgeにまとめる

それぞれのコールごとに、playerとcomを比較してありえない数字の組み合わせをはじいている

1.1に比べて試行回数が減っているようにみえる


【ToDo】
1.1と1.3で比較して性能をはかってみる

ほんとうは前回comと今回comをくらべるべき

前回comを格納してstrategyで参照するしくみをつくる

strategyコピペだから改善の余地あり

defはわけて本体にimportにしようかな…