import json,pathlib,sys,urllib.parse
p=pathlib.Path(__file__).resolve().parent.parent; a=json.loads((p/'data/trials.json').read_text()); ids=set();errors=[]
required=['id','name','category','patientGroup','molecular','design','n','arms','primaryEndpoint','results','safety','limitations','sources','verifiedAt','comparisonGroup']
for t in a:
 id=t.get('id','MISSING')
 if id in ids:errors.append(f'{id}: duplicate id')
 ids.add(id)
 for k in required:
  if not t.get(k):errors.append(f'{id}: missing {k}')
 for s in t.get('sources',[]):
  if not s.get('title') or urllib.parse.urlparse(s.get('url','')).scheme not in ['http','https']:errors.append(f'{id}: invalid citation')
 for c in t.get('resultCharts',[]):
  for k in ['title','endpoint','timepoint','population','unit','sourceUrl']:
   if not c.get(k):errors.append(f'{id}: chart missing {k}')
  if urllib.parse.urlparse(c.get('sourceUrl','')).scheme not in ['http','https']:errors.append(f'{id}: invalid chart source')
  for ar in c.get('arms',[]):
   if not isinstance(ar.get('value'),(int,float)):errors.append(f'{id}: chart non-numeric arm')
   if c.get('unit')=='%' and not 0<=ar.get('value',-1)<=100:errors.append(f'{id}: percent outside 0..100')
   lo,hi=ar.get('ciLow'),ar.get('ciHigh')
   if (lo is None)!=(hi is None) and not any(k in c.get('note','') for k in ['未达到','not reached','not estimable','NE','NR']):errors.append(f'{id}: incomplete CI without source explanation')
   if lo is not None and hi is not None and (lo>hi or not lo<=ar['value']<=hi):errors.append(f'{id}: inconsistent CI')
  if c.get('hr') is not None and c['hr']<=0:errors.append(f'{id}: HR must be positive')
  if c.get('hrCiLow') is not None and c.get('hrCiHigh') is not None and not c['hrCiLow']<=c['hr']<=c['hrCiHigh']:errors.append(f'{id}: HR outside CI')
 for arm in t.get('scheme',{}).get('arms',[]):
  if not arm.get('label') or not arm.get('steps'):errors.append(f'{id}: empty scheme arm')
print(json.dumps({'trials':len(a),'schemes':sum(bool(t.get('scheme')) for t in a),'charts':sum(len(t.get('resultCharts',[])) for t in a),'errors':errors},ensure_ascii=False,indent=2));sys.exit(bool(errors))
