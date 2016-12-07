import logging
from pyDatalog import pyDatalog, pyEngine
pyEngine.Logging = True
logging.basicConfig(level=logging.INFO)
pyDatalog.create_terms('missing_log,pre,post,missing_log_provYTUBLKEOXZCLZIID,pre_provOACULFKPDBTNQQFC,post_provPKMRFIGTCHKXUROW,node,log,node_provVVTULPTTZNNSFSRB,log_provINPLHASNVVEBXZKQ,log_provQSMZJETQMMXMEPHJ,log_provQVOGPUAWVYOKXRCH,clock,bcast,crash')
pyDatalog.create_terms('A,Pl,SndTime,X,Node,Neighbor,SndTime,Pload,Node2,DelivTime,Node1,_')
pyDatalog.create_terms('THISISAWILDCARDFWHSABIAWPXMEKQN,THISISAWILDCARDKBWJHWCLMAGCJCXO,THISISAWILDCARDMJEXOGONGZVBILZJ,THISISAWILDCARDGSCCDKFEGGJHELDZ,THISISAWILDCARDXENFLUKWRISICTWP,THISISAWILDCARDBLXUQQFIUTNMEXTS,THISISAWILDCARDQMJEGXDUNENYINQS,THISISAWILDCARDFMYQPUNEMYSQHAHS,THISISAWILDCARDZGCJEWKJLTPNIVBR,THISISAWILDCARDFZCCDKCNHRDYRWKW,THISISAWILDCARDVEOWXLFJNPTZXXRL,THISISAWILDCARDLZCAMFCBMHRKTMBL,THISISAWILDCARDCTBTQRSADYLPSLFM,THISISAWILDCARDYUOVSRXXGOCLUHNT,THISISAWILDCARDLBCPNSAYDZDOGQAI,THISISAWILDCARDMDZJPRZWXHNGPAQF,THISISAWILDCARDSBHMYPQUWESNYTFF,THISISAWILDCARDHCGFICCPSRHOEMRV,THISISAWILDCARDRXSXSOYCIQYYGMQG,THISISAWILDCARDMVRDOTOKOFADGJLR')
pyDatalog.assert_fact('node',"a","b",1)
pyDatalog.assert_fact('node',"a","c",1)
pyDatalog.assert_fact('node',"b","a",1)
pyDatalog.assert_fact('node',"b","c",1)
pyDatalog.assert_fact('node',"c","a",1)
pyDatalog.assert_fact('node',"c","b",1)
pyDatalog.assert_fact('bcast',"a","hello",1)
pyDatalog.assert_fact('clock','a','a','1','2')
pyDatalog.assert_fact('clock','a','b','1','2')
pyDatalog.assert_fact('clock','a','c','1','2')
pyDatalog.assert_fact('clock','a','d','1','2')
pyDatalog.assert_fact('clock','b','a','1','2')
pyDatalog.assert_fact('clock','b','b','1','2')
pyDatalog.assert_fact('clock','b','c','1','2')
pyDatalog.assert_fact('clock','b','d','1','2')
pyDatalog.assert_fact('clock','c','a','1','2')
pyDatalog.assert_fact('clock','c','b','1','2')
pyDatalog.assert_fact('clock','c','c','1','2')
pyDatalog.assert_fact('clock','c','d','1','2')
pyDatalog.assert_fact('clock','d','a','1','2')
pyDatalog.assert_fact('clock','d','b','1','2')
pyDatalog.assert_fact('clock','d','c','1','2')
pyDatalog.assert_fact('clock','d','d','1','2')
pyDatalog.assert_fact('clock','a','a','2','3')
pyDatalog.assert_fact('clock','a','b','2','3')
pyDatalog.assert_fact('clock','a','c','2','3')
pyDatalog.assert_fact('clock','a','d','2','3')
pyDatalog.assert_fact('clock','b','a','2','3')
pyDatalog.assert_fact('clock','b','b','2','3')
pyDatalog.assert_fact('clock','b','c','2','3')
pyDatalog.assert_fact('clock','b','d','2','3')
pyDatalog.assert_fact('clock','c','a','2','3')
pyDatalog.assert_fact('clock','c','b','2','3')
pyDatalog.assert_fact('clock','c','c','2','3')
pyDatalog.assert_fact('clock','c','d','2','3')
pyDatalog.assert_fact('clock','d','a','2','3')
pyDatalog.assert_fact('clock','d','b','2','3')
pyDatalog.assert_fact('clock','d','c','2','3')
pyDatalog.assert_fact('clock','d','d','2','3')
pyDatalog.assert_fact('clock','a','a','3','4')
pyDatalog.assert_fact('clock','a','b','3','4')
pyDatalog.assert_fact('clock','a','c','3','4')
pyDatalog.assert_fact('clock','a','d','3','4')
pyDatalog.assert_fact('clock','b','a','3','4')
pyDatalog.assert_fact('clock','b','b','3','4')
pyDatalog.assert_fact('clock','b','c','3','4')
pyDatalog.assert_fact('clock','b','d','3','4')
pyDatalog.assert_fact('clock','c','a','3','4')
pyDatalog.assert_fact('clock','c','b','3','4')
pyDatalog.assert_fact('clock','c','c','3','4')
pyDatalog.assert_fact('clock','c','d','3','4')
pyDatalog.assert_fact('clock','d','a','3','4')
pyDatalog.assert_fact('clock','d','b','3','4')
pyDatalog.assert_fact('clock','d','c','3','4')
pyDatalog.assert_fact('clock','d','d','3','4')
(missing_log(A,Pl,SndTime)) <= (log(X,Pl,SndTime)) & (node(X,A,SndTime)) & (~(log(A,Pl,SndTime)) )& ( clock(X,X,SndTime,THISISAWILDCARDFWHSABIAWPXMEKQN))
(pre(X,Pl,SndTime)) <= (log(X,Pl,SndTime)) & (~(bcast(X,Pl,1)) )& (~(crash(X,X,THISISAWILDCARDKBWJHWCLMAGCJCXO,SndTime)) )& ( clock(X,X,SndTime,THISISAWILDCARDMJEXOGONGZVBILZJ))
(post(X,Pl,SndTime)) <= (log(X,Pl,SndTime)) & (~(missing_log(THISISAWILDCARDGSCCDKFEGGJHELDZ,Pl,SndTime)) )& ( clock(X,X,SndTime,THISISAWILDCARDXENFLUKWRISICTWP))
(missing_log_provYTUBLKEOXZCLZIID(A,Pl,X,SndTime)) <= (log(X,Pl,SndTime)) & (node(X,A,SndTime)) & (~(log(A,Pl,SndTime)) )& (clock(X,X,SndTime,THISISAWILDCARDBLXUQQFIUTNMEXTS))
(pre_provOACULFKPDBTNQQFC(X,Pl,SndTime)) <= (log(X,Pl,SndTime)) & (~(bcast(X,Pl,1)) )& (~(crash(X,X,THISISAWILDCARDQMJEGXDUNENYINQS,SndTime)) )& (clock(X,X,SndTime,THISISAWILDCARDFMYQPUNEMYSQHAHS))
(post_provPKMRFIGTCHKXUROW(X,Pl,SndTime)) <= (log(X,Pl,SndTime)) & (~(missing_log(THISISAWILDCARDZGCJEWKJLTPNIVBR,Pl,SndTime)) )& (clock(X,X,SndTime,THISISAWILDCARDFZCCDKCNHRDYRWKW))
(node(Node,Neighbor,SndTime+1)) <= (node(Node,Neighbor,SndTime)) & ( clock(Node,THISISAWILDCARDVEOWXLFJNPTZXXRL,SndTime,THISISAWILDCARDLZCAMFCBMHRKTMBL))
(log(Node,Pload,SndTime+1)) <= (log(Node,Pload,SndTime)) & ( clock(Node,THISISAWILDCARDCTBTQRSADYLPSLFM,SndTime,THISISAWILDCARDYUOVSRXXGOCLUHNT))
(log(Node2,Pload,DelivTime)) <= (bcast(Node1,Pload,SndTime)) & (node(Node1,Node2,SndTime)) & ( clock(Node1,Node2,SndTime,DelivTime))
(log(Node,Pload,SndTime)) <= (bcast(Node,Pload,SndTime)) & ( clock(Node,Node,SndTime,THISISAWILDCARDLBCPNSAYDZDOGQAI))
(node_provVVTULPTTZNNSFSRB(Node,Neighbor,SndTime+1,SndTime)) <= (node(Node,Neighbor,SndTime)) & (clock(Node,THISISAWILDCARDMDZJPRZWXHNGPAQF,SndTime,THISISAWILDCARDSBHMYPQUWESNYTFF))
(log_provINPLHASNVVEBXZKQ(Node,Pload,SndTime+1,SndTime)) <= (log(Node,Pload,SndTime)) & (clock(Node,THISISAWILDCARDHCGFICCPSRHOEMRV,SndTime,THISISAWILDCARDRXSXSOYCIQYYGMQG))
(log_provQSMZJETQMMXMEPHJ(Node2,Pload,DelivTime,Node1,SndTime)) <= (bcast(Node1,Pload,SndTime)) & (node(Node1,Node2,SndTime)) & (clock(Node1,Node2,SndTime,DelivTime))
(log_provQVOGPUAWVYOKXRCH(Node,Pload,SndTime)) <= (bcast(Node,Pload,SndTime)) & (clock(Node,Node,SndTime,THISISAWILDCARDMVRDOTOKOFADGJLR))
print ( pre(X,Pl,SndTime) )
print ( post(X,Pl,SndTime) )
