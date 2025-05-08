# Order Status Workflow Flowchart

This document provides a comprehensive visual representation of all order status transitions in the ShopLo Backend system.

## Complete Order Status Flowchart

```mermaid
flowchart TD
    %% Main statuses
    NEW[1. New\ntype: order]
    REJECTED[2. Rejected\ntype: order]
    CANCELED[3. Canceled\ntype: order]
    ACCEPTED[4. Accepted\ntype: order]
    READY[5. Ready for Delivery\ntype: order]
    DELIVERING[6. Delivering\ntype: order]
    DELIVERED[7. Delivered\ntype: order]
    DELIVERY_DONE[15. Delivery Done\ntype: order]
    DELAYED[16. Delayed\ntype: order]
    
    %% Delivery statuses
    REJECT_DELIVERY[8. Reject Delivery\ntype: delivery]
    ACCEPT_DELIVERY[9. Accept Delivery\ntype: delivery]
    TIMEOUT[10. Time Out\ntype: delivery]
    
    %% Refund statuses
    REFUND_NEW[11. New\ntype: refund]
    REFUND_REJECTED[12. Rejected\ntype: refund]
    REFUND_ACCEPTED[13. Accepted\ntype: refund]
    REFUND_REPLACED[14. Replaced\ntype: refund]
    
    %% Scheduled Order Process statuses
    WAITING_ADMIN[17. Waiting Admin Approval\ntype: scheduled_order]
    WAITING_CLIENT[18. Waiting Client Approval\ntype: scheduled_order]
    WAITING_DELIVERY[19. Waiting Delivery Assignment\ntype: scheduled_order]
    DELIVERY_ASSIGNED[20. Delivery Assigned\ntype: scheduled_order]
    
    %% Individual Scheduled Delivery statuses
    SCHED_WAITING[21. Waiting\ntype: scheduled]
    SCHED_DELIVERED[22. Delivered\ntype: scheduled]
    SCHED_CANCELED[23. Canceled\ntype: scheduled]
    
    %% Regular Order Flow
    NEW --> REJECTED
    NEW --> CANCELED
    NEW --> ACCEPTED
    NEW --> DELAYED
    DELAYED --> CANCELED
    DELAYED --> READY
    ACCEPTED --> READY
    READY --> DELIVERING
    DELIVERING --> DELIVERED
    DELIVERED --> DELIVERY_DONE
    
    %% Delivery Person Actions
    subgraph "Delivery Request Process"
        ACCEPT_DELIVERY
        REJECT_DELIVERY
        TIMEOUT
    end
    
    READY -.-> ACCEPT_DELIVERY
    READY -.-> REJECT_DELIVERY
    READY -.-> TIMEOUT
    ACCEPT_DELIVERY -.-> DELIVERING
    REJECT_DELIVERY -.-> READY
    TIMEOUT -.-> READY
    
    %% Refund Process
    subgraph "Refund Process"
        REFUND_NEW --> REFUND_REJECTED
        REFUND_NEW --> REFUND_ACCEPTED
        REFUND_ACCEPTED --> REFUND_REPLACED
    end
    
    DELIVERED -.-> REFUND_NEW
    
    %% Scheduled Order Flow
    subgraph "Scheduled Order Process"
        WAITING_ADMIN --> WAITING_CLIENT
        WAITING_CLIENT --> WAITING_DELIVERY
        WAITING_DELIVERY --> DELIVERY_ASSIGNED
    end
    
    %% Integration with main order status
    NEW -.-> WAITING_ADMIN
    WAITING_ADMIN -.-> CANCELED
    WAITING_CLIENT -.-> CANCELED
    DELIVERY_ASSIGNED -.-> DELIVERING
    
    %% Individual Scheduled Deliveries
    subgraph "Individual Scheduled Deliveries"
        SCHED_WAITING --> SCHED_DELIVERED
        SCHED_WAITING --> SCHED_CANCELED
    end
    
    DELIVERY_ASSIGNED -.-> SCHED_WAITING
    
    %% Style
    classDef orderStatus fill:#f9f,stroke:#333,stroke-width:2px
    classDef deliveryStatus fill:#bbf,stroke:#333,stroke-width:2px
    classDef refundStatus fill:#fbb,stroke:#333,stroke-width:2px
    classDef scheduledStatus fill:#bfb,stroke:#333,stroke-width:2px
    classDef scheduledDeliveryStatus fill:#ffb,stroke:#333,stroke-width:2px
    
    class NEW,REJECTED,CANCELED,ACCEPTED,READY,DELIVERING,DELIVERED,DELIVERY_DONE,DELAYED orderStatus
    class REJECT_DELIVERY,ACCEPT_DELIVERY,TIMEOUT deliveryStatus
    class REFUND_NEW,REFUND_REJECTED,REFUND_ACCEPTED,REFUND_REPLACED refundStatus
    class WAITING_ADMIN,WAITING_CLIENT,WAITING_DELIVERY,DELIVERY_ASSIGNED scheduledStatus
    class SCHED_WAITING,SCHED_DELIVERED,SCHED_CANCELED scheduledDeliveryStatus
```

## Explanation of Flowchart Elements

### Node Types
- **Solid boxes with pink background**: Regular order statuses (type: order)
- **Solid boxes with blue background**: Delivery request statuses (type: delivery)
- **Solid boxes with red background**: Refund process statuses (type: refund)
- **Solid boxes with green background**: Scheduled order process statuses (type: scheduled_order)
- **Solid boxes with yellow background**: Individual scheduled delivery statuses (type: scheduled)

### Connection Types
- **Solid arrow lines**: Direct status transitions within the same process
- **Dotted arrow lines**: Connections between different status types/processes

## Detailed Order Status Workflow

### Regular Order Flow
1. Order starts with "New" status
2. Can transition to "Rejected", "Canceled", "Accepted", or "Delayed"
3. "Accepted" orders move to "Ready for Delivery"
4. "Ready for Delivery" orders move to "Delivering" (once a delivery person is assigned)
5. "Delivering" orders move to "Delivered" (when delivery person marks as delivered)
6. "Delivered" orders move to "Delivery Done" (final confirmation)

### Delivery Request Process
- When an order is "Ready for Delivery", delivery requests are sent
- Delivery persons can "Accept" or "Reject" the request
- If no response, request times out
- When accepted, order moves to "Delivering" status

### Scheduled Order Process
- Scheduled orders have a dual status system
- Main order status remains "New" until delivery starts
- Process status moves through:
  1. "Waiting Admin Approval"
  2. "Waiting Client Approval" (after admin approves)
  3. "Waiting Delivery Assignment" (after client approves)
  4. "Delivery Assigned" (when delivery person is assigned)
- After delivery assignment, the main order status follows the regular flow

### Individual Scheduled Deliveries
- Each scheduled delivery has its own status in the "scheduled" type
- Starts as "Waiting"
- Can be marked as "Delivered" or "Canceled"

### Refund Process
- Can be initiated for "Delivered" orders
- Has its own status flow: New → Accepted/Rejected
- Accepted refunds can be marked as "Replaced"

## Common Status Transitions

1. **Cancellation**: 
   - From "New" or "Delayed" → "Canceled"
   - Scheduled orders can be canceled at "Waiting Admin Approval" or "Waiting Client Approval"

2. **Delivery Assignment**:
   - "Ready for Delivery" → "Delivering" (via delivery request acceptance)
   - "Waiting Delivery Assignment" → "Delivery Assigned" (for scheduled orders)

3. **Completion**:
   - "Delivered" → "Delivery Done"
   - "Scheduled Waiting" → "Scheduled Delivered" 