from .anchor_head_single import AnchorHeadSingle
from .anchor_head_template import AnchorHeadTemplate
from .anchor_head_rdiou import AnchorHeadRDIoU
from .anchor_head_rdiou_3cat import AnchorHeadRDIoU_3CAT

__all__ = {
    'AnchorHeadTemplate': AnchorHeadTemplate,
    'AnchorHeadSingle': AnchorHeadSingle,
    'AnchorHeadRDIoU': AnchorHeadRDIoU,
    'AnchorHeadRDIoU_3CAT': AnchorHeadRDIoU_3CAT
}
