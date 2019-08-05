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
	if (!xdr_int(xdrs, &(pBlock->physInd))) return 0;
	if (!xdr_int(xdrs, &(pBlock->logInd))) return 0;
	if (!xdr_int(xdrs, &(pBlock->dummy))) return 0;

	return xdr_vector(xdrs,&(pBlock->block),sBlock,sizeof(char),xdr_char);
}

int
xdr_Request(XDR *xdrs, Request *req)
{
	if (!xdr_int(xdrs,&(req->lev)))     return 0;
	if (!xdr_int(xdrs,&(req->physInd))) return 0;
    if (!xdr_int(xdrs,&(req->logInd)))  return 0;

	return xdr_vector(xdrs,&(req->block),sBlock,sizeof(char),xdr_char);
}

