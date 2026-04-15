backend/
├── src/
│   ├── config/             # Cấu hình DB, Passport, AWS S3, Redis
│   ├── controllers/        # Xử lý logic HTTP request
│   ├── models/             # Schema Database (User, Auction, Bid, Product)
│   ├── routes/             # Định nghĩa các API endpoints
│   ├── services/           # Logic nghiệp vụ (Tính toán giá, kiểm tra thời gian)
│   ├── middlewares/        # Kiểm tra Auth (JWT), phân quyền (Admin/User)
│   ├── sockets/            # Xử lý logic Real-time (Socket.io cho Bidding)
│   ├── workers/            # Cron jobs (Tự động kết thúc đấu giá, gửi email)
│   ├── utils/              # Các hàm bổ trợ (Format tiền tệ, xử lý ngày tháng)
│   └── app.js              # Điểm khởi đầu của server
├── .env                    # Biến môi trường (DB_URL, SECRET_KEY)
└── package.json


frontend/
├── public/                 # Ảnh, icons, fonts tĩnh
├── src/
│   ├── components/         # Các component dùng chung
│   │   ├── AuctionCard/    # Thẻ hiển thị sản phẩm đấu giá
│   │   ├── Countdown/      # Bộ đếm ngược thời gian
│   │   └── BidHistory/     # Danh sách người đã trả giá
│   ├── hooks/              # Custom hooks (useSocket, useAuth)
│   ├── pages/              # Các trang chính (Home, Auction Detail, Profile)
│   ├── services/           # Gọi API từ Backend (Axios)
│   ├── store/              # Quản lý state toàn cục (Redux/Zustand)
│   └── styles/             # Tailwind CSS hoặc SCSS
├── .env
└── package.json