#include <rpc/rpc.h>
#include "go.h"

int
xdr_serverConf(XDR *xdrs, serverConf *sc)
{

	if (!xdr_int(xdrs, &(sc->numLev))) return 0;

    return xdr_vector(xdrs,&(sc->levnBits),MaxNumLev,sizeof(int),xdr_int);

}

int
xdr_physPlainBlock(XDR *xdrs, physPlainBlock *pBlock)
{

	if (!xdr_int(xdrs, &(pBlock->lev))) return 0;
	if (!xdr_int(xdrs, &(pBlock->logInd))) return 0;
	if (!xdr_int(xdrs, &(pBlock->dummy))) return 0;
	return xdr_vector(xdrs,&(pBlock->block),sBlock,sizeof(char),xdr_char);
}

int
xdr_wRequest(XDR *xdrs, wRequest *wr)
{
	if (!xdr_int(xdrs,&(wr->lev)))     return 0;
	if (!xdr_int(xdrs,&(wr->physInd))) return 0;
	return xdr_reference(xdrs,&wr->pb,sizeof(physPlainBlock),xdr_physPlainBlock);
}

int
xdr_rRequest(XDR *xdrs, rRequest *rr)
{
	if (!xdr_int(xdrs,&(rr->lev)))     return 0;
	return xdr_int(xdrs,&(rr->physInd));
}

