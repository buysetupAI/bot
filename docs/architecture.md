# Architecture

## Overview
The system is composed of several modules:
- Wallet Manager: Handles wallet configurations and limits.
- Solana Client: Interacts with the Solana RPC API.
- AI Decision: Provides token and strategy recommendations.
- Strategies: Implements trading logic like DCA.

## Workflow
1. The bot fetches configurations from `config/`.
2. AI Decision generates token recommendations.
3. Strategy Manager executes the recommended strategies.
4. Orders are placed via Solana Client.
5. Wallet limits are checked before executing any orders.
